from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class VisitorAccessConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.visitor_access"
    verbose_name = _("Visitor Access")
    


