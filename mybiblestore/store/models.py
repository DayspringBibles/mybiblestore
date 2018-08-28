# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class insides(models.Model):

	language = models.CharField(max_length=200)
	translation = models.CharField(max_length=200)
	columns = models.CharField(max_length=200)
	reference_bible = models.BooleanField()
	study_bible = models.BooleanField()
	verse_style = models.CharField(max_length=200)
	concordance = models.BooleanField()
	maps = models.BooleanField()
	width = models.FloatField(max_length=200)
	height = models.FloatField(max_length=200)
	size_range = models.CharField(max_length=200)
	source = models.CharField(max_length=200)
	price = models.FloatField(max_length=200)
	labor = models.FloatField(max_length=200)
	text = models.CharField(max_length=200)
	leadtime = models.FloatField(max_length=200)
	name = models.CharField(max_length=200)
	keywords = models.CharField(max_length=2000)
	short_description = models.CharField(max_length=2000,null=True)


class leather(models.Model):

	name = models.CharField(max_length=200)
	color = models.CharField(max_length=50)
	animal = models.CharField(max_length=100)
	price = models.FloatField(max_length=50)
	source = models.CharField(max_length=2000)
	description = models.CharField(max_length=2000)


