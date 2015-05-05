from django.conf.urls import patterns, url
from apps.editor import views

urlpatterns = patterns('',
	url(r'^$', editor.Index, name = 'index'),
	url(r'^load/$', views.Load, name = 'load'),
)
