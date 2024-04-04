from django.contrib import admin

from .models import (
    Town,
    Galery_image,
    Speaker,
    Program_part,
    Tag,
    Event,
    Galery_imageEvent,
    SpeakerEvent,
    Program_partEvent,
    ParticipantEvent,
    TagEvent
)


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    pass


@admin.register(Galery_image)
class Galery_imageAdmin(admin.ModelAdmin):
    pass


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    pass


@admin.register(Program_part)
class Program_partAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class Galery_imageEventInline(admin.TabularInline):
    model = Galery_imageEvent


class SpeakerEventInline(admin.TabularInline):
    model = SpeakerEvent


class Program_partEventInline(admin.TabularInline):
    model = Program_partEvent


class ParticipantEventInline(admin.TabularInline):
    model = ParticipantEvent


class TagEventInline(admin.TabularInline):
    model = TagEvent


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [
        Galery_imageEventInline, SpeakerEventInline,
        Program_partEventInline, ParticipantEventInline,
        TagEventInline
    ]