from django.conf.urls import url
from . import views

#app_name = 'emails'
urlpatterns = [
    url(r'^new/$', views.EmailCreateView.as_view(), name='new'),
    url(r'^sent$', views.sent),
	url(r'^$', views.ListView.as_view(), name='list'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/edit/$', views.EmailUpdateView.as_view()),
	url(r'^(?P<pk>[0-9]+)/delete/$', views.EmailDeleteView.as_view()),
	url(r'^test/(?P<we>\w+)/$', views.TestView.as_view()),
	url(r'^http/(?P<abcd>\w+)/$', views.TestHttp.as_view()),
]

