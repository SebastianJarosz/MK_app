# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Operation, OperationDescription
from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'MK_apps/index.html')

def operations(request):
	operations = Operation.objects.order_by('text')
	context = {'operations': operations}
	return render(request, 'MK_apps/operations.html', context)

def operation(request, operation_id):
	operation = Operation.objects.get(id = operation_id)
	operationDescriptions = operation.operationdescription_set.all()
	context = {'operation':operation, 'operationDescriptions': operationDescriptions}
	return render(request, 'MK_apps/operation.html', context)	
	
