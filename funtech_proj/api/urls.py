from django.urls import include, path
# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view
# from rest_framework import permissions
# from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from api.views import (
    # ProfileLists,
    EventViewSet,
)

v1_router = DefaultRouter()


v1_router.register("events", EventViewSet, basename="events")


# schema_view = get_schema_view(
#     openapi.Info(
#         title="Funtech API",
#         default_version="v1",
#         description="Документация _",
#         terms_of_service="URL страницы с пользовательским соглашением",
#         # contact=openapi.Contact(email="admin@kadmin.ru"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path("v1/", include(v1_router.urls)),
    # path("v1/lists/", ProfileLists.as_view(), name="lists"),
    # path(
    #     "docs/swagger/",
    #     schema_view.with_ui("swagger", cache_timeout=0),
    #     name="schema-swagger-ui",
    # ),
    # path(
    #     "docs/redoc/",
    #     schema_view.with_ui("redoc", cache_timeout=0),
    #     name="schema-redoc",
    # ),
]

# urlpatterns += [
#    url(r'^swagger(?P<format>\.json|\.yaml)$', 
#        schema_view.without_ui(cache_timeout=0), name='schema-json'),
#    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), 
#        name='schema-swagger-ui'),
#    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), 
#        name='schema-redoc'),
# ]
