# Generated by Django 2.0.2 on 2018-02-23 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('triptailor', '0003_auto_20180223_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traveler',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='traveler',
            name='last_name',
        ),
    ]