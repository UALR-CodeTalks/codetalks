from django.conf.urls import patterns, include, url
from apps.browse import views

urlpatterns = patterns('',
	url(r'^$', views.Index, name = 'index'),
)
