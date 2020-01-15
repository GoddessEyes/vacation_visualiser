"""Роути для API приложения. Схема API."""

from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from vacation_visualiser.api.employee.auth_urls import urlpatterns
from vacation_visualiser.api.employee.urls import router as employee_router
from vacation_visualiser.api.vacation.urls import router as vacation_router


app_name = 'v1'

schema_view = get_schema_view(
    openapi.Info(
        title='Vacation Visualiser API',
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = (
    path('auth/', include(urlpatterns)),
    path('', include(vacation_router.urls)),
    path('', include(employee_router.urls)),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
)
