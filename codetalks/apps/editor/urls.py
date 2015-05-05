from django.conf.urls import patterns, url
from apps.editor import views

urlpatterns = patterns('',
	url(r'^load/$', views.Load, name = 'load'),
)
