import uuid
import string
import random
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth import get_user_model
from django.db import models
from core_apps.users.models import User


User = get_user_model()



STATUS_CHOICES = (
    ('active', 'Active'),
    ('completed', 'Completed'),
    ('pending', 'Pending'),
)

GENDER_CHOICES = (
    ('', 'Select gender'),
    ('male', 'Male'),
    ('female', 'Female'),
)

# Generate access code for visitor
def generate_access_code():
    # Generate a random 5-character access code
    pass_code = ''.join(random.choices(string.digits, k=5))
    return pass_code

class VisitorAccessRequest(models.Model):
    access_code = models.CharField(max_length=5, unique=True, default=generate_access_code)
    visitor_name = models.CharField(max_length=100, verbose_name=_("Visitor Name"))
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, verbose_name=_("Gender"))
    vehicle_registration = models.CharField(max_length=20, null=True, blank=True, verbose_name=_("Vehicle Registration"))
    additional_information = models.TextField(blank=True, null=True, verbose_name=_("Additional Information"))
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator', verbose_name=_("Creator"))
    date_created = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    is_resolved = models.BooleanField(default=False)
    accepted_date = models.DateTimeField(null=True, blank=True)
    closed_date = models.DateTimeField(null=True, blank=True)
    request_status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name=_("Request Status"))


    def __str__(self):
        return self.visitor_name

