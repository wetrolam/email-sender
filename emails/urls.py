from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new$', views.new),
    url(r'^send$', views.send)
]
