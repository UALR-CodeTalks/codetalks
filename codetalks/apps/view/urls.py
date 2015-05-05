from django.conf.urls import patterns, include, url
from apps.view import views

urlpatterns = patterns('',
	url(r'^$', views.Index, name = 'index'),
	url(r'^gethashes/$', views.GetHashes, name = 'gethashes')
)
