# homepage/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
   
	url(r'^$', 'homepage.views.home', name='home'),
	# url(r'^(?P<trav_slug>[-\w]+)/$', 'homepage.views.travdetail', name='trav'),
)
