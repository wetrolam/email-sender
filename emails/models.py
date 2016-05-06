from django.db import models

class Email(models.Model):
	template = models.TextField()
