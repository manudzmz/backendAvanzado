# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
