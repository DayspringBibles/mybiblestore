# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-24 23:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_leather_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leather',
            old_name='amimal',
            new_name='animal',
        ),
    ]
