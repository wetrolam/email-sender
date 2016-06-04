from .models import EmailSource
from django.shortcuts import render
from django.views import generic
from django.http.response import HttpResponse, HttpResponseRedirect
from django.db.models import Q
import logging
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from .forms import EmailSourceForm
import csv
from .email_utility import create_emails

logger = logging.getLogger(__name__)

#avoid access to an email created by a different user
class EmailOwnerAccessMixin(object):
	def dispatch(self, request, *args, **kwargs):
		email = self.get_object()
		if self.request.user == email.user:
			return super(EmailOwnerAccessMixin, self).dispatch(request, *args, **kwargs)
		else:
			raise PermissionDenied


class EmailCreateView(generic.edit.CreateView):
	#model = EmailSource
	form_class = EmailSourceForm
	template_name = 'emails/email_form.html'
	#fields = ['subject', 'text', 'specificData']
	success_url = '/emails'
	heading = 'Vytvorenie noveho emailu'

	def form_valid(self, form):
		form.instance.user = self.request.user
		result = super(EmailCreateView, self).form_valid(form)
		if 'saveAndConfirm' in self.request.POST:
			return HttpResponseRedirect('/emails/' + form.instance.id.__str__() + '/confirm')
		return result

def sent(request):
	return render(request, 'emails/sent.html')

class ListView(LoginRequiredMixin, generic.ListView):
	# model = EmailSource
	template_name = 'emails/list.html'
	context_object_name = 'email_list'
	heading = 'Zoznam emailov'
	#queryset = EmailSource.objects.order_by('user')
	#queryset = EmailSource.objects.filter(user__username='p1')

	def get_queryset(self):
		logger.debug("vypis zoznamu emailov")
		print("vypis zoznam emailov b")
		return EmailSource.objects.filter(user=self.request.user.id)

class DetailView(EmailOwnerAccessMixin, generic.DetailView): #UserPassesTestMixin
	model = EmailSource
	template_name = 'emails/detail.html'
	all_emails = EmailSource.objects.all()
	heading = 'Detail emailu'
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

	# def test_func(self):
	# 	email = self.get_object() #EmailSource.objects.get(id=self.kwargs['pk'])
	# 	return self.request.user == email.user

class EmailUpdateView(EmailOwnerAccessMixin, generic.edit.UpdateView):
	model = EmailSource #needed because self.get_object()
	form_class = EmailSourceForm
	template_name = 'emails/email_form.html'
	success_url = '/emails'
	heading = 'Uprava emailu'

	def form_valid(self, form):
		result = super(EmailUpdateView, self).form_valid(form)
		if 'saveAndConfirm' in self.request.POST:
			return HttpResponseRedirect('/emails/' + self.kwargs['pk'].__str__() + '/confirm')
		return result

	# a sent email can't be updated
	def dispatch(self, request, *args, **kwargs):
		email = self.get_object()
		if email.isSent():
			messages.error(request, "You can not update a sent email")
			raise PermissionDenied
		else:
			return super(EmailUpdateView, self).dispatch(request, *args, **kwargs)

class EmailDuplicateView(EmailOwnerAccessMixin, generic.edit.UpdateView):
	model = EmailSource
	form_class = EmailSourceForm
	template_name = 'emails/email_form.html'
	success_url = '/emails'
	heading = 'Vytvorenie emailu z kopie'

	def form_valid(self, form):
		emailSource = EmailSource()
		emailSource.user = form.instance.user
		emailSource.subject = form.instance.subject
		emailSource.text = form.instance.text
		emailSource.specificData = form.instance.specificData
		emailSource.save()
		if 'saveAndConfirm' in self.request.POST:
			return HttpResponseRedirect('/emails/' + emailSource.id.__str__() + '/confirm')
		return HttpResponseRedirect(self.success_url)

class EmailDeleteView(EmailOwnerAccessMixin, generic.edit.DeleteView):
	model = EmailSource
	template_name = 'emails/email_delete.html'
	success_url = '/emails'
	heading = 'Potvrdenie vymazania emailu emailu'

	# a sent email can't be deleted
	def dispatch(self, request, *args, **kwargs):
		email = self.get_object()
		if email.isSent():
			messages.error(request, "You can not delete a sent email")
			raise PermissionDenied
		else:
			return super(EmailDeleteView, self).dispatch(request, *args, **kwargs)

class SendConfirmView(EmailOwnerAccessMixin, generic.edit.UpdateView):
	template_name = 'emails/email_send_confirm.html'
	model = EmailSource
	fields = []

	def get_context_data(self, **kwargs):
		context = super(SendConfirmView, self).get_context_data(**kwargs)
		context['sender'] = self.request.user
		email = EmailSource.objects.get(pk = self.kwargs['pk'])
		context['emails'] = create_emails(email.subject, email.text, email.specificData)
		return context

	def form_valid(self, form):
		if 'sendNow' in self.request.POST:
			form.instance.sendEmailAndSaveSentTime()
			return HttpResponseRedirect('/emails')
		else:
			return HttpResponseRedirect('/emails/' + self.kwargs['pk'].__str__() + '/edit')

	# a sent email can't be send again
	def dispatch(self, request, *args, **kwargs):
		email = self.get_object()
		if email.isSent():
			messages.error(request, "You can not update a sent email")
			raise PermissionDenied
		else:
			return super(SendConfirmView, self).dispatch(request, *args, **kwargs)

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

class TestViewWithForm(generic.edit.CreateView):
	#model = EmailSource
	form_class = EmailSourceForm
	template_name = 'emails/email_form.html'
	#fields = ['subject', 'text', 'specificData']
	success_url = '/emails'

	def form_valid(self, form):
		form.instance.user = self.request.user
		result = super(TestViewWithForm, self).form_valid(form)
		if 'saveAndSendNow' in self.request.POST:
			form.sendEmailAndSaveSentTime()
		return result