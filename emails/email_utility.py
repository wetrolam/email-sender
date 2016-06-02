# from .models import EmailSource
# from datetime import datetime
import csv

class EmailData:

	def __init__(self, receiver, subject, text):
		self.receiver = receiver
		self.subject = subject
		self.text = text


	def __unicode__(self):
		return 'receiver: ' + self.receiver + '\nsubject: ' + self.subject + '\ntext:\n' + self.text

	def __str__(self):
		return self.__unicode__().encode('utf-8')


def create_emails(template_subject, template_text, specific_data):
	email_data = []
	reader = csv.DictReader(specific_data.splitlines(), delimiter=";")
	columns = reader.fieldnames
	for line in reader:
		receiver = line['email']
		subject  = template_subject
		text     = template_text
		for name in columns:
			subject = subject.replace("{{"+name+"}}", line[name])
			text    = text.replace("{{"+name+"}}", line[name])
		email_data.append(EmailData(receiver, subject, text))

	# print("---- zozname emailov (start) ----")
	# for e in email_data:
	# 	print(e.__unicode__())
	# 	print("-----")
	# print("---- zozname emailov (stop) ----")
	return email_data


def csv_validator(text):
	reader = csv.DictReader(text.splitlines(),  delimiter=';')
	columns = reader.fieldnames
	numColumns = columns.__len__()
	if numColumns == 0:
		raise ValidationError(_('enter at least 1 column'))
	if 'email' not in columns:
		raise ValidationError(_('the name of a one column has to be "email"'))
	for line in reader:
		if line.__len__() != numColumns:
			raise ValidationError(_('too many columns in line: (%(line)s)'), params={'line': line.__str__()})
		for name in columns:
			if line[name] == None:
				raise ValidationError(_('"%(name)s" is not defined in line: %(line)s'), params={'name': name, 'line': line.__str__()})

