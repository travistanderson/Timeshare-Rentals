# pages/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template, redirect_to

urlpatterns = patterns('',
	(r'^(?P<url>.*)$', 'pages.views.pager'),
)

