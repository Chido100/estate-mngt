from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _ 
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from core_apps.common.models import TimeStampedModel

User = get_user_model()


#class StreetName(models.Model):
#    street_name = models.CharField(verbose_name=_("Street Name"), max_length=100, unique=True)

#    class Meta:
#        verbose_name_plural = "Street Names"
    
 #   def __str__(self):
#        return self.street_name


#class HouseNumber(models.Model):
#    house_number = models.CharField(verbose_name=_("House Number"), max_length=10)

#    class Meta:
#       verbose_name_plural = "House Numbers"

#    def __str__(self):
#        return self.house_number


def get_user_username(instance: "Profile") -> str:
    return instance.user.username



class Profile(TimeStampedModel):
    class Gender(models.TextChoices):
        FEMALE = ("female", _("Female"))
        MALE = ("male", _("Male"))
        OTHER = ("other", _("Other"))

    class Occupation(models.TextChoices):
        #MANAGEMENT = ("management", _("Management"))
        #SECURITY = ("security", _("Security"))
        RESIDENT = ("resident", _("Resident"))
        RETAILER = ("retailer", _("Retailer"))


    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = CloudinaryField(verbose_name=_("Avatar"), blank=True, null=True)
    gender = models.CharField(choices=Gender.choices, default=Gender.OTHER, max_length=10, verbose_name=_("Gender"))
    bio = models.TextField(verbose_name=_("Bio"), blank=True, null=True)
    occupation = models.CharField(choices=Occupation.choices, default=Occupation.RESIDENT, max_length=20, verbose_name=_("Occupation"))
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, default="+2348000000000")
    #street_name = models.ForeignKey(StreetName, on_delete=models.CASCADE, related_name="street")
    #house_number = models.ForeignKey(HouseNumber, on_delete=models.CASCADE, max_length=10, related_name="house")
    slug = AutoSlugField(populate_from=get_user_username, unique=True)

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    



