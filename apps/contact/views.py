# contact/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from photologue.models import Photo
from contact.forms import ContactForm
from django.conf import settings
from mailer import send_mail


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		# toemail = 'tanderson@hisg.org'
		toemail = 'modernarrangements@gmail.com'
		toemail2 = 'travistanderson@gmail.com'
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			subject = "Message from the TSR Website"
			content = "From:" + name + ": " + email + "\n\n" + 'Topic - ' + form.cleaned_data['subject'] + '\n\n\n' + form.cleaned_data['content']
			send_mail(subject, content, email,[toemail,toemail2,])
			return HttpResponseRedirect('/contact/success')
		else:
			form = ContactForm(request.POST)
			return render_to_response('contact/contact.html', {'form':form,},context_instance = RequestContext(request),)
	else:
		form = ContactForm()
		m = '.'
	return render_to_response(
		'contact/contact.html', {'form':form,},context_instance = RequestContext(request),)


def contactsuccess(request):
	m = 'Success'
	return render_to_response('contact/contactsuccess.html', {'message': m,},context_instance = RequestContext(request),)
