from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
#	url('^', include('django.contrib.auth.urls')),
	url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}),
	url(r'^logout/$', auth_views.logout, {'template_name': 'accounts/logout.html'}),
	#url(r'^logout/$', auth_views.logout_then_login), #, {'template_name': 'accounts/logout.html'}),
	url(r'^create/$', views.create_account),
	url(r'^profile/$', views.AccountProfileView.as_view()),
	url(r'^password_change/$', auth_views.password_change, {'template_name': 'accounts/password_change.html', 'post_change_redirect': '/accounts/profile'}), #, name = 'password_change'),
	url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'accounts/password_reset.html'}), #, 'post_reset_redirect': '/accounts/login'}), #, name='password_reset'),
	url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'accounts/password_reset_done.html'}, name='password_reset_done'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {'template_name': 'accounts/reset.html'}, name='password_reset_confirm'),
	url(r'^reset/done/$', auth_views.password_reset_complete, {'template_name': 'accounts/reset_done.html'}, name='password_reset_complete'),
]
