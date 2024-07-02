from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import VisitorAccessRequest


class VisitorAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorAccessRequest
        fields = ['visitor_name', 'gender', 'vehicle_registration', 'additional_information']

        