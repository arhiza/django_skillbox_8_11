# Generated by Django 2.2 on 2021-11-04 23:12

import app_users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0004_auto_20211102_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(blank=True, upload_to=app_users.models.Profile.user_directory_path, verbose_name='Аватар'),
        ),
    ]
