import logging
import random

from data import factories as f
from django.core.management import BaseCommand
from factory.django import DjangoModelFactory
from users.models import User

from funtech_proj.settings import PRELOAD_DATA_BATCH_SIZE as SIZE

logging.basicConfig(level=logging.INFO)


def get_or_create_batch(_class: DjangoModelFactory, **kwargs) -> list:
    if _class._meta.model.objects.exists():
        logging.info(f"{_class.__name__} data already exists... exiting.")
        return _class._meta.model.objects.all()
    logging.info(f"=Loading {_class.__name__} data")
    created = _class.create_batch(SIZE, **kwargs)
    logging.info(f"=== {created}")
    return created


def get_random(
    items: list[f.DjangoModelFactory], size: int = 3
) -> list[f.DjangoModelFactory]:
    return (
        sorted(random.choices(items, k=size), key=lambda item: item.id)
        if size < len(items)
        else items
    )


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        events = get_or_create_batch(
            f.EventFactory,
            stacks=get_random(get_or_create_batch(f.StackFactory)),
            specializations=get_random(get_or_create_batch(f.SpecializationFactory)),
        )
        users = reversed(User.objects.all())
        for event in events:
            f.Gallery_imageFactory(event=event)
            f.Program_partFactory(event=event)
            f.SpeakerFactory(event=event)

        for event, user in zip(events, users):
            f.ParticipantEventFactory(participant=user, event=event)