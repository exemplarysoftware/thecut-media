# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from django.conf.urls import url


urlpatterns = [
    url(r'^django-admin/', admin.site.urls),
    ]

