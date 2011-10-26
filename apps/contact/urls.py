# contact/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^success$', 'contact.views.contactsuccess', name="contactsuccess"),   
	url(r'^$', 'contact.views.contact', name='contact'),
)


