# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Operation (models.Model):
	text = models.CharField(max_length=200)
	
	def __str__(self):
		return self.text
		
class OperationDescription (models.Model):
	operation = models.ForeignKey(Operation)
	text = models.CharField(max_length=200)
	
	class Meta:
		verbose_name_plural = 'entry'
	
	def __str__(self):
		return self.text
	
		
class Tool (models.Model):
	operationDescription = models.ForeignKey(OperationDescription)
	operationDescription = models.ManyToManyField(OperationDescription)
	text = models.CharField(max_length=200)
	
	class Meta:
		verbose_name_plural = 'tools'
	
	def __str__(self):
		return self.text

