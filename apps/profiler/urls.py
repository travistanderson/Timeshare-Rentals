# profiler/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
	url(r'^create-new-user/$', 'profiler.views.newuser', name='newuser'),
	url(r'^user-created/$', 'profiler.views.usercreated', name='usercreated'),
	
	url(r'^$','profiler.views.proindex', name='proindex',),
	url(r'^(?P<user_id>\d+)/$', 'profiler.views.profile', name='profile'),
)





# url(r'^choose-an-ad/$', 'profiler.views.chart', name='chart'),
# url(r'^create-premium/$', 'profiler.views.premiumcreate', name='premiumcreate'),
# url(r'^create-free/$', 'profiler.views.freecreate', name='freecreate'),
# url(r'^create-add-pictures/(?P<ad_id>\d+)/$', 'profiler.views.createpictures', name='createpictures'),
# url(r'^create-add-resort/(?P<newresort>[-\w]+)/$', 'profiler.views.createnewresort', name='createnewresort'),