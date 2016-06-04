from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
#	url('^', include('django.contrib.auth.urls')),
	url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}),
	url(r'^logout/$', auth_views.logout, {'template_name': 'accounts/logout.html'}),
	url(r'^create/$', views.create_account),
	url(r'^profile/$', views.profile)
]
