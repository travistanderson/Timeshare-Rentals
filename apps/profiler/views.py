# profiler/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template import defaultfilters
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from datetime import datetime, timedelta
import hashlib
from profiler.forms import NewUserForm
from photologue.models import Photo, Gallery
from ts.models import Ad, Resort


def newuser(request):
	if request.method == 'POST': # If the form has been submitted...
		form = NewUserForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			thepass = hashlib.sha1()							# Process the data in form.cleaned_data
			thepass.update(form.cleaned_data['password1'])
			password = thepass.hexdigest()
			user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password1'])
			user.save()
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/profile/user-created/') # Redirect after POST
				else:
					return HttpResponseRedirect('/profile/account-disabled/') # Redirect after POST
	else:
		form = NewUserForm() # An unbound form
	return render_to_response('registration/newuser.html', {'form': form,})	


@login_required
def usercreated(request):
	return render_to_response('registration/usercreated.html',context_instance = RequestContext(request),)


def allusers(request):
	u = User.objects.all()
	return render_to_response('profiler/index.html', {'users':u,},context_instance = RequestContext(request),)


@login_required	
def profile(request,user_id):
	u = User.objects.get(id=user_id)
	if u == request.user:
		me = 1
	else:
		me = 0
	ads = Ad.objects.filter(creator=u)
	paidmodads = Ad.objects.filter(creator=u,paid=True,premod=True)
	return render_to_response('profiler/profile.html', {"theuser":u,'ads':ads,'paidmodads':paidmodads,'me':me,},context_instance = RequestContext(request),)
	
	
	
	
