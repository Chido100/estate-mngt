from django.contrib import admin
from .models import VisitorAccessRequest


@admin.register(VisitorAccessRequest)
class VisitorAccessAdmin(admin.ModelAdmin):
    list_display = ['visitor_name', 'date_created', 'creator', 'assigned_to']
