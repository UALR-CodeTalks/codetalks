from django.conf.urls import patterns, url
from apps.view import views

urlpatterns = patterns('',
	url(r'^$', views.Index, name = 'index'),
)
