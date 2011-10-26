# profiler/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
	url(r'^create-new-user/$', 'profiler.views.newuser', name='newuser'),
	url(r'^user-created/$', 'profiler.views.usercreated', name='usercreated'),
	
	url(r'^$','profiler.views.allusers', name='allusers',),
	url(r'^(?P<user_id>\d+)/$', 'profiler.views.profile', name='profile'),
)



