# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-30 04:08
from __future__ import unicode_literals

from django.db import migrations, models
import uploads.models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0006_auto_20180130_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='document',
            field=models.FileField(default='/media/acdc.txt', upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='image',
            field=models.ImageField(default='/media/acdc_profile.jpg', upload_to=uploads.models.profile_image_path),
        ),
    ]
