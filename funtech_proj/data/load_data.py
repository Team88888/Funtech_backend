import logging
import random

from django.conf import settings
from factory.django import DjangoModelFactory
from users.models import User

from .events_factories import (
    EventFactory,
    Gallery_imageFactory,
    Program_partFactory,
    SpeakerFactory,
)
from .shared_factories import SpecializationFactory, StackFactory

logging.basicConfig(level=logging.INFO)


def get_or_create_batch(_class: DjangoModelFactory, **kwargs) -> list:
    if _class._meta.model.objects.exists():
        logging.info(f"{_class.__name__} data already exists... exiting.")
        return _class._meta.model.objects.all()
    logging.info(f"=Loading {_class.__name__} data")
    created = _class.create_batch(settings.PRELOAD_DATA_BATCH_SIZE, **kwargs)
    logging.info(f"=== {created}")
    return created


def get_random(
    items: list[DjangoModelFactory], size: int = 3
) -> list[DjangoModelFactory]:
    return (
        sorted(random.choices(items, k=size), key=lambda item: item.id)
        if size < len(items)
        else items
    )


def load_db(*args, **kwargs):
    stacks = get_or_create_batch(StackFactory)
    specializations = get_or_create_batch(SpecializationFactory)
    events = set(get_or_create_batch(EventFactory))
    users = set(User.objects.all())
    for event, user in zip(events, users):
        user.stacks.add(*get_random(stacks))
        user.specializations.add(*get_random(specializations))
        event.participants.add(*get_random(list(users)))
        event.stacks.add(*get_random(stacks))
        event.specializations.add(*get_random(specializations))
        Gallery_imageFactory(event=event)
        Program_partFactory(event=event)
        SpeakerFactory(event=event)
