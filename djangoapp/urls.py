from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^templado/', include('templado.urls', namespace='templado')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
)
