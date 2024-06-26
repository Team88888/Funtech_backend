from api_v2 import views as v
from django.urls import include, path
from rest_framework.routers import DefaultRouter

ROUTES = (
    ("towns", v.TownViewSet),
    ("specializations", v.SpecializationViewSet),
    ("stack", v.StackViewSet),
    ("events_short", v.EventShortViewSet),
    ("events/closest", v.ClosestEventsViewsSet),
    ("events", v.EventViewSet),
    ("participants", v.ParticipantEventViewSet),
)
"""
    ("forms", v.FormViewSet),
    ("themes", v.ThemeViewSet),
    ("speakers", v.SpeakerViewSet),
    ("images", v.GalleryImageViewSet),
    ("program_parts", v.Program_partViewSet),
    ("events/interesting", v.MayBeInterestingViewSet),
    ("events", v.EventViewSet),
    ("users", v.UserViewSet),
"""


v2_router = DefaultRouter()
for url_prefix, view_set in ROUTES:
    v2_router.register(url_prefix, view_set, basename=url_prefix)

urlpatterns = [
    path("/", include(v2_router.urls)),
]
