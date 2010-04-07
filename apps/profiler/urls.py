# profiler/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
   
	url(r'^$','profiler.views.proindex', name='proindex',),
	# url(r'^choose-an-ad/$', 'profiler.views.chart', name='chart'),
	# url(r'^create-premium/$', 'profiler.views.premiumcreate', name='premiumcreate'),
	# url(r'^create-free/$', 'profiler.views.freecreate', name='freecreate'),
	# url(r'^create-add-pictures/(?P<ad_id>\d+)/$', 'profiler.views.createpictures', name='createpictures'),
	# url(r'^create-add-resort/(?P<newresort>[-\w]+)/$', 'profiler.views.createnewresort', name='createnewresort'),
	url(r'^(?P<user_id>\d+)/$', 'profiler.views.profile', name='profile'),
)
