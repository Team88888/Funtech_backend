from api.views import EventViewSet
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

v1_router = DefaultRouter()

v1_router.register("events", EventViewSet, basename="events")

schema_view = get_schema_view(
    openapi.Info(
        title="Funtech API",
        default_version="v1",
        description="Документация",
        terms_of_service="URL страницы с пользовательским соглашением",
        # contact=openapi.Contact(email="admin@kadmin.ru"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "swagger<format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
