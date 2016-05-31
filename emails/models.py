from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.urlresolvers import reverse
from datetime import datetime

class EmailSource(models.Model):
	user = models.ForeignKey(User)
	subject = models.CharField(max_length=200)
	template = models.TextField()
	specificData = models.TextField()
	sentDateTime = models.DateTimeField(null=True, blank=True) #http://stackoverflow.com/questions/11351619/how-to-make-djangos-datetimefield-optional

	def isSent(self):
		return self.sentDateTime is not None

	# def get_absolute_url(self):
	# 	return reverse('email-detail', kwargs={'pk': self.pk})

	def sendEmailAndSaveSentTime(self):
		receiver = self.specificData
		print("posielam email ------------->>---------- " + receiver)
		#send_mail('Subject here', 'Here is the message.', 'from@example.com', [receiver], fail_silently=False)
		self.sentDateTime = datetime.now()
		self.save()
