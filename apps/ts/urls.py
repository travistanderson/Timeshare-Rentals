# ts/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
   
	url(r'^$','ts.views.adlist', name='adlist',),
	url(r'^view/(?P<ad_id>\d+)/$', 'ts.views.addetail', name='ad_detail'),
	url(r'^edit/(?P<ad_id>\d+)/$', 'ts.views.adedit', name='ad_edit'),
	url(r'^choose-an-ad/$', 'ts.views.chart', name='chart'),
	url(r'^create/ad/(?P<adtype>[-\w]+)/$', 'ts.views.newadcreate', name='newadcreate'),
	url(r'^create/picture/(?P<ad_id>\d+)/$', 'ts.views.createpictures', name='createpictures'),	
	url(r'^(?P<ad_id>\d+)/$', 'ts.views.addetail', name='addetail'),
)
