# Generated by Django 5.0.6 on 2024-06-22 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="street_name",
        ),
        migrations.RemoveField(
            model_name="user",
            name="house_number",
        ),
        migrations.DeleteModel(
            name="AllStreets",
        ),
        migrations.DeleteModel(
            name="HouseNumbers",
        ),
    ]