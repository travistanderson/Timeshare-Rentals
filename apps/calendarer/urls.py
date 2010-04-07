# calendarer/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
   
	url(r'^$', 'calendarer.views.calendar', name='calendar'),
	# url(r'^(?P<trav_slug>[-\w]+)/$', 'homepage.views.travdetail', name='trav'),
)
