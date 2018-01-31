# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-31 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0007_auto_20180130_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='document',
            field=models.FileField(default='/media/no_text.txt', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='upload',
            name='image',
            field=models.ImageField(default='/media/no_image.png', upload_to=b''),
        ),
    ]
