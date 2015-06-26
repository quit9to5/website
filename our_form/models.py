import datetime
from django.db import models
from django.utils import timezone

class information(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name
