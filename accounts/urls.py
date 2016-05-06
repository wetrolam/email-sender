from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
#	url('^', include('django.contrib.auth.urls')),
	url(r'^login$', auth_views.login, {'template_name': 'accounts/login.html'}),
	url(r'^logout$', auth_views.logout),
	url(r'^profile$', views.profile)
]
