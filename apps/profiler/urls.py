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
	url(r'^messages/(?P<user_id>\d+)/$', 'profiler.views.messages', name='messages'),
	url(r'^messages/(?P<user_id>\d+)/(?P<message_id>\d+)/$', 'profiler.views.message', name='message'),
	url(r'^messages/(?P<user_id>\d+)/compose/(?P<object_id>\d+)/(?P<reco>[-\w]+)/$', 'profiler.views.compose', name='compose'),
	url(r'^settings/(?P<user_id>\d+)/$', 'profiler.views.usersettings', name='usersettings'),
	url(r'^(?P<user_id>\d+)/$', 'profiler.views.profile', name='profile'),
)



