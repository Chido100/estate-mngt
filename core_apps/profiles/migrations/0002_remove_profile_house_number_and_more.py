# Generated by Django 5.0.6 on 2024-06-25 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="house_number",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="street_name",
        ),
        migrations.DeleteModel(
            name="HouseNumber",
        ),
        migrations.DeleteModel(
            name="StreetName",
        ),
    ]