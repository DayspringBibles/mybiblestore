# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import insides
from .models import leather

admin.site.register(insides)
admin.site.register(leather)