# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 14:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relationship',
            old_name='follower',
            new_name='origin',
        ),
        migrations.RenameField(
            model_name='relationship',
            old_name='following',
            new_name='target',
        ),
    ]
