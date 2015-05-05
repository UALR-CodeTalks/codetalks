from django.conf.urls import patterns, url
from apps.editor import views

urlpatterns = patterns('',
	url(r'^$', views.Index, name = 'index'),
	url(r'^newproject/$', views.GetNewProject, name = 'newproject'),
	url(r'^savecode/$', views.SaveCode, name = 'savecode'),
	url(r'^altername/$', views.AlterName, name = 'altername'),
	url(r'^vote/$', views.Vote, name = 'vote')
)
