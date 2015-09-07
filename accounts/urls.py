from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^register/$' , 'accounts.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login', kwargs={'template_name': 'accounts/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',name='logout', kwargs= {'template_name': 'accounts/logout.html'}),
)
