# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-30 00:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='url1',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='url2',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='url3',
        ),
    ]
