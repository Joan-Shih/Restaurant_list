# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 01:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ['price']},
        ),
    ]