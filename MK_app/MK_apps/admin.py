# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from MK_apps.models import Operation, OperationDescription ,Tool

admin.site.register(Operation)
admin.site.register(Tool)
admin.site.register(OperationDescription)
