from .models import EmailSource
from django.shortcuts import render
from django.views import generic
from django.http.response import HttpResponse, HttpResponseRedirect
from django.db.models import Q

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
	# model = EmailSource
	template_name = 'emails/list.html'
	context_object_name = 'email_list'
	#queryset = EmailSource.objects.order_by('user')
	queryset = EmailSource.objects.filter(user__username='p1')

	# def get_queryset(self):
	# 	return EmailSource.objects.filter(user=self.request.user.id)

class DetailView(generic.DetailView):
	model = EmailSource
	template_name = 'emails/detail.html'
	all_emails = EmailSource.objects.all()
	#queryset = EmailSource.objects.filter(Q(id=1) | Q(id=2) | Q(id=3) | Q(id=4))
	#allow_empty = True

	# def all_emails(self):
	# 	return EmailSource.objects.all()

	# def get_queryset(self):
	# 	return EmailSource.objects.filter(id=1)

	# def get_context_data(self, **kwargs):
	# 	context = super(DetailView, self).get_context_data(**kwargs)
		#context['all_emails'] = EmailSource.objects.all()
		# return context

class TestView(generic.TemplateView):
	template_name = 'emails/test.html'
	#conext_object_name = 'all_emails'
	all_emails = EmailSource.objects.all()
	udaj = 'ahoj'

	def get_context_data(self, **kwargs):
		context = super(TestView, self).get_context_data(**kwargs)
		context['we'] = kwargs['we']
		return context

class TestHttp(generic.View):
	def get(self, request, abcd):
		return HttpResponse("vratene metodou get " + abcd)

	def put(self, request):
		#return HttpResponse("vratene metodou post")
		return HttpResponseRedirect('/success/')