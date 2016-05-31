from django import forms
from .models import EmailSource
from datetime import datetime

class EmailSourceForm(forms.ModelForm):
	class Meta:
		model = EmailSource
		fields = ['subject','template', 'specificData']

	#file = forms.FileField(label='scv subor')

	# def save(self):
	# 	result = super(EmailSourceForm, self).save(commit=False)
	# 	result.user = self.user
	# 	result.sentDateTime = datetime.now()
	# 	result.save()
	# 	return result

	def sendEmailAndSaveSentTime(self):
		self.instance.sendEmailAndSaveSentTime()
