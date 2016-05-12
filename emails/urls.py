from django.conf.urls import url
from . import views

#app_name = 'emails'
urlpatterns = [
    url(r'^new$', views.NewView.as_view(), name='new'),
    url(r'^send$', views.send),
	url(r'^$', views.ListView.as_view(), name='list'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]

