from django.conf.urls import patterns, include, url
from apps.view import views

urlpatterns = patterns('',
	url(r'^gethashes/$', views.GetHashes, name = 'gethashes')
)
