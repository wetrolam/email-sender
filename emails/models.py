from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.urlresolvers import reverse
from datetime import datetime
import csv
from django.core.validators import validate_slug
from .email_utility import create_emails, csv_validator
from django.core.mail import send_mail

class EmailSource(models.Model):
	user = models.ForeignKey(User)
	subject = models.CharField(max_length=200)
	text = models.TextField()
	specificData = models.TextField(validators=[csv_validator])
	sentDateTime = models.DateTimeField(null=True, blank=True) #http://stackoverflow.com/questions/11351619/how-to-make-djangos-datetimefield-optional

	def isSent(self):
		return self.sentDateTime is not None

	# def get_absolute_url(self):
	# 	return reverse('email-detail', kwargs={'pk': self.pk})

	def sendEmailAndSaveSentTime(self):
		sender = self.user.email
		print("---- posielam emaily od " + sender + " ----")
		emails = create_emails(self.subject, self.text, self.specificData)
		for e in emails:
			print("    -> " + e.receiver)
			send_mail(e.subject, e.text, sender, [e.receiver], fail_silently=False)
			#send_mail('Subject here', 'Here is the message.', 'from@example.com', [receiver], fail_silently=False)
		self.sentDateTime = datetime.now()
		self.save()
