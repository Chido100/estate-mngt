
from django.contrib import admin
from django.conf import settings
from django.urls import path
from drf_yasg.views import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.info(
        title="Signala EMS API",
        default_version="v1",
        description="Estate Management System",
        contact=openapi.Contact(email="api.imperfect@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("redoc/",schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header= "Signala EMS Admin"
admin.site.site_title = "Signala EMS Admin Portal"
admin.site.index_title = "Welcome to Signala EMS Admin Portal"

