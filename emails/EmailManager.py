from .models import EmailSource
from datetime import datetime

def sendEmail(emailSource):
	receiver = emailSource.specificData
	print("posielam email ------------->>---------- " + receiver)
	#send_mail('Subject here', 'Here is the message.', 'from@example.com', [receiver], fail_silently=False)
	emailSource.sentDateTime = datetime.now()
	emailSource.save()