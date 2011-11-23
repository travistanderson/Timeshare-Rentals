# ts/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^edit/(?P<ad_id>\d+)/$', 'ts.views.adedit', name='ad_edit'),
	url(r'^delete/(?P<ad_id>\d+)/$', 'ts.views.addelete', name='ad_delete'),
	url(r'^choose-an-ad/$', 'ts.views.chart', name='chart'),
	url(r'^create/ad/(?P<adtype>[-\w]+)/$', 'ts.views.newadcreate', name='newadcreate'),
	url(r'^create/picture/(?P<ad_id>\d+)/$', 'ts.views.createpictures', name='createpictures'),
	url(r'^create/picture/order/(?P<ad_id>\d+)/$', 'ts.views.photorder', name='photorder'),
	url(r'^resorts/(?P<resort_slug>[-\w]+)/$', 'ts.views.resortdetail', name='resortdetail'),
	url(r'^resorts/$','ts.views.resortlist', name='resortlist',),
	url(r'^(?P<ad_id>\d+)/(?P<ad_slug>[-\w]+)/$', 'ts.views.addetail', name='addetail'),
	url(r'^$','ts.views.adlist', name='adlist',),
)
