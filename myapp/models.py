from django.db import models

# Create your models here.

class Student(models.Model):
	name=models.CharField(max_length=80)
	roll=models.IntegerField()
	marks=models.IntegerField()
	dob = models.DateField()
	place = models.CharField(max_length=80)
	email = models.EmailField()
