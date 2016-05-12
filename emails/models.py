from django.db import models
from django.contrib.auth.models import User
from django import forms

class EmailSource(models.Model):
	user = models.ForeignKey(User)
	subject = models.CharField(max_length=200)
	template = models.TextField()
	specificData = models.TextField()
