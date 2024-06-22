from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm


User = get_user_model()

class UserChangeForm(BaseUserChangeForm):
    class Meta(BaseUserChangeForm.Meta):
        model = User
        fields = ["first_name", "last_name", "street_name", "house_number", "email"]


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = ["first_name", "last_name", "street_name", "house_number", "email"]
    
    error_messages = {
        "duplicate_username": "A user with that username already exists.",
        "duplicate_email": "A user with that email address already exists."
    }

    def clean_email(self) -> str:
        
