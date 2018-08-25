# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-24 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='insides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=200)),
                ('translation', models.CharField(max_length=200)),
                ('columns', models.CharField(max_length=200)),
                ('reference_bible', models.BooleanField()),
                ('study_bible', models.BooleanField()),
                ('verse_style', models.CharField(max_length=200)),
                ('concordance', models.CharField(max_length=200)),
                ('maps', models.CharField(max_length=200)),
                ('width', models.FloatField(max_length=200)),
                ('height', models.FloatField(max_length=200)),
                ('size_range', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=200)),
                ('price', models.FloatField(max_length=200)),
                ('labor', models.FloatField(max_length=200)),
                ('text', models.CharField(max_length=200)),
                ('images', models.CharField(max_length=1000)),
                ('leadtime', models.FloatField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=2000)),
            ],
        ),
    ]
