from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Medication(models.Model):
	generic_name = models.CharField(max_length=128)
	brand_names = models.CharField(max_length=128)
	user = models.ForeignKey(User)
	units = models.CharField(max_length=128)



class Event(models.Model):
	date = models.DateTimeField()
	event_type = models.TextField()
	description = models.TextField()
	dosage = models.TextField()
	user = models.ForeignKey(User)
	medication = models.ForeignKey(Medication)