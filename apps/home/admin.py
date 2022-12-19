# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import website

# Register your models here.

class Adminwebsite(admin.ModelAdmin):
    model = website
    list_display = ('id','author', 'website_url', 'website_blocked')


admin.site.register(website, Adminwebsite)
