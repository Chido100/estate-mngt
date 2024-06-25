# Generated by Django 5.0.6 on 2024-06-25 10:26

import autoslug.fields
import cloudinary.models
import core_apps.profiles.models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="HouseNumber",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "house_number",
                    models.CharField(max_length=10, verbose_name="House Number"),
                ),
            ],
            options={
                "verbose_name_plural": "House Numbers",
            },
        ),
        migrations.CreateModel(
            name="StreetName",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "street_name",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Street Name"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Street Names",
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "avatar",
                    cloudinary.models.CloudinaryField(
                        blank=True, max_length=255, null=True, verbose_name="Avatar"
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("female", "Female"),
                            ("male", "Male"),
                            ("other", "Other"),
                        ],
                        default="other",
                        max_length=10,
                        verbose_name="Gender",
                    ),
                ),
                ("bio", models.TextField(blank=True, null=True, verbose_name="Bio")),
                (
                    "occupation",
                    models.CharField(
                        choices=[("resident", "Resident"), ("retailer", "Retailer")],
                        default="resident",
                        max_length=20,
                        verbose_name="Occupation",
                    ),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        default="+2348000000000",
                        max_length=30,
                        region=None,
                        verbose_name="Phone Number",
                    ),
                ),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False,
                        populate_from=core_apps.profiles.models.get_user_username,
                        unique=True,
                    ),
                ),
                (
                    "house_number",
                    models.ForeignKey(
                        max_length=10,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="house",
                        to="profiles.housenumber",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "street_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="street",
                        to="profiles.streetname",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at", "updated_at"],
                "abstract": False,
            },
        ),
    ]