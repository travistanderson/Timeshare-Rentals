# ts/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
   
	url(r'^$','ts.views.adlist', name='adlist',),
	url(r'^view/(?P<ad_id>\d+)/$', 'ts.views.addetail', name='ad_detail'),
	url(r'^edit/(?P<ad_id>\d+)/$', 'ts.views.adedit', name='ad_edit'),
	url(r'^choose-an-ad/$', 'ts.views.chart', name='chart'),
	url(r'^create-premium/$', 'ts.views.premiumcreate', name='premiumcreate'),
	url(r'^create-free/$', 'ts.views.freecreate', name='freecreate'),
	url(r'^create-add-pictures/(?P<ad_id>\d+)/$', 'ts.views.createpictures', name='createpictures'),
	url(r'^create-add-resort-branch/(?P<newresort>[-\w]+)/(?P<ad_id>\d+)/$', 'ts.views.createnewresortbranch', name='createnewresortbranch'),
	url(r'^create-add-resort/(?P<newresort>[-\w]+)/(?P<ad_id>\d+)/$', 'ts.views.createnewresort', name='createnewresort'),
	url(r'^create-add-country/(?P<newresort>[-\w]+)/(?P<ad_id>\d+)/$', 'ts.views.createnewcountry', name='createnewcountry'),	
	url(r'^(?P<ad_id>\d+)/$', 'ts.views.addetail', name='addetail'),
)
