from .models import EmailSource
from django.shortcuts import render
from django.views import generic

class NewView(generic.DetailView):
	model = EmailSource
	template_name = 'emails/new.html'
	#queryset = EmailSource.objects.filter(id=1)

	def get_queryset(self):
	# def get_object(self):
		print("volam NewView qet queryset ")
		return EmailSource.objects.filter(id=2)
		#return EmailSource()

def send(request):
	return render(request, 'emails/send.html')

class ListView(generic.ListView):
	template_name = 'emails/list.html'
	context_object_name = 'email_list'

	def get_queryset(self):
		return EmailSource.objects.filter(user=self.request.user.id)

class DetailView(generic.DetailView):
	model = EmailSource
	template_name = 'emails/detail.html'

	# def get_queryset(self):
	# 	return EmailSource.objects.filter(id=1)

