from .models import EmailSource
from django.shortcuts import render
from django.views import generic
from django.http.response import HttpResponse, HttpResponseRedirect
from django.db.models import Q
import logging
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from datetime import datetime

logger = logging.getLogger(__name__)

class EmailCreateView(generic.edit.CreateView):
	model = EmailSource
	template_name = 'emails/email_form.html'
	fields = ['subject', 'template', 'specificData']
	success_url = '/emails'

	def form_valid(self, form):
		logging.debug("email vytvoreny")
		print("email vytvoreny")
		form.instance.user = self.request.user
		result = super(EmailCreateView, self).form_valid(form)
		if 'saveAndSendNow' in self.request.POST:
			self.send_mail(form)
		return result

	def form_invalid(self, form):
		logging.debug("email chybne definovany")
		print("email chybne definovany")
		return super(EmailCreateView, self).form_invalid(form)

	def send_mail(self, form):
		receiver = form.instance.specificData
		print("posielam email ------------->>---------- " + receiver)
		#send_mail('Subject here', 'Here is the message.', 'from@example.com', [receiver], fail_silently=False)
		form.instance.sentDateTime = datetime.now()
		form.instance.save()
		#some problem with push

def sent(request):
	return render(request, 'emails/sent.html')

class ListView(generic.ListView):
	# model = EmailSource
	template_name = 'emails/list.html'
	context_object_name = 'email_list'
	#queryset = EmailSource.objects.order_by('user')
	#queryset = EmailSource.objects.filter(user__username='p1')

	def get_queryset(self):
		logger.debug("vypis zoznamu emailov")
		print("vypis zoznam emailov b")
		return EmailSource.objects.filter(user=self.request.user.id)

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

class EmailUpdateView(generic.UpdateView):
	model = EmailSource
	template_name = 'emails/email_update_form.html'
	fields = ['subject', 'template', 'specificData']
	success_url = '/emails'

class EmailDeleteView(generic.DeleteView):
	model = EmailSource
	template_name = 'emails/email_delete.html'
	success_url = '/emails'

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