import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.utils.translation import gettext_lazy as _ 
from core_apps.users.managers import UserManager


# Customised validator just for future purpose -- Django already provides username validator by default
class UsernameValidator(validators.RegexValidator):
    regex = r"^[\w.@+-]+\Z"
    message = _(
        "Your username is not valid. Ausername can only contain letters, numbers, a dot, "
        "@ symbol, + symbol and a hyphen "
    )
    flag = 0


# All streets list
class AllStreets(models.Model):
    street = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = _("All Streets")
        verbose_name_plural = _("Streets")

    def __str__(self):
        return self.street

# All house numbers list
class HouseNumbers(models.Model):
    house = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = _("House Numbers")
        verbose_name_plural = _("House Numbers")
    
    def __str__(self):
        return self.house




class User(AbstractUser):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=50, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=50, verbose_name=_("Last Name"))
    street_name = models.ForeignKey(AllStreets, on_delete=models.CASCADE, related_name='all_streets', default='street')
    house_number = models.ForeignKey(HouseNumbers, on_delete=models.CASCADE, related_name='house', default='00')
    email = models.EmailField(unique=True, verbose_name=_("Email Address"), db_index=True)
    username = models.CharField(max_length=50, verbose_name=_("Username"), unique=True, validators=[UsernameValidator])

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username, first_name, last_name, street_name, house_number"]

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-date_joined"]
    
    @property
    def get_full_name(self) -> str:
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()
