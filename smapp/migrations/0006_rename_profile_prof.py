# Generated by Django 5.0.3 on 2024-04-12 18:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smapp', '0005_alter_profile_location'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Prof',
        ),
    ]
