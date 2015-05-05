from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'apps.home.home.Index'),
    url(r'^editor/', include('apps.editor.urls', namespace = 'editor')),
    url(r'^view/', include('apps.view.urls', namespace = 'view')),
    url(r'^admin/', include(admin.site.urls)),
]
