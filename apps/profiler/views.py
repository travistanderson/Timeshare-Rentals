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
from profiler.models import Mess
from profiler.forms import NewUserForm, MessForm
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
	return render_to_response('profiler/profiles.html', {'users':u,},context_instance = RequestContext(request),)


@login_required	
def profile(request,user_id):
	u = User.objects.get(id=user_id)
	if u == request.user:
		me = 1
	else:
		me = 0
	ads = Ad.objects.filter(creator=u)
	mess = Mess.objects.filter(receiver=u,unread=True)
	paidmodads = Ad.objects.filter(creator=u,paid=True,premod=True)
	return render_to_response('profiler/profile.html', {"theuser":u,'ads':ads,'paidmodads':paidmodads,'me':me,'mess':mess},context_instance = RequestContext(request),)
	
	
@login_required	
def messages(request,user_id):
	u = User.objects.get(id=user_id)
	if not u == request.user:
		return HttpResponseRedirect(reverse('messages',args=[request.user.id]))
	mess = Mess.objects.filter(receiver=u)
	unread = Mess.objects.filter(receiver=u,unread=True)
	return render_to_response('profiler/messages.html', {"theuser":u,'mess':mess,'unread':unread,},context_instance = RequestContext(request),)


@login_required	
def message(request,user_id,message_id):
	u = User.objects.get(id=user_id)
	if not u == request.user:
		return HttpResponseRedirect(reverse('messages',args=[request.user.id]))
	mess = Mess.objects.get(id=message_id)
	mess.unread = False
	mess.save()
	return render_to_response('profiler/message.html', {"theuser":u,'mess':mess},context_instance = RequestContext(request),)


# @login_required	
def compose(request,user_id,object_id,reco):
	if user_id != '0':
		u = User.objects.get(id=user_id)
		wf = 1
		if not u == request.user:
			return HttpResponseRedirect(reverse('messages',args=[request.user.id]))
	else:
		u = request.user
		wf = 0
	reply = False
	if reco == 'reply':
		re = get_object_or_404(Mess,id=object_id)
		initial = {'subject':'Re: ' + re.subject,}
		reply = True
	else:
		re = get_object_or_404(Ad,id=object_id)
		initial = {'subject':'Question about ad: ' + re.name,}
	if request.method == 'POST': # If the form has been submitted...
		form = MessForm(wf,request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			message = form.save(commit=False)
			if wf==1:		# it is from an authenticated user
				message.sender = request.user
				if reply:
					message.receiver = re.sender
					message.replied = re
				else:
					message.receiver = re.creator
				message.save()
				return HttpResponseRedirect(reverse('messages',args=[user_id])) # Redirect after POST	
			else:		# it is from some random user
				message.email = form.cleaned_data['emailer']
				message.name = form.cleaned_data['namer']
				message.receiver = re.creator
				message.save()
				return HttpResponseRedirect(reverse('home')) # Redirect after POST
	else:
		form = MessForm(wf,initial=initial) # An unbound form
	return render_to_response('profiler/compose.html', {'theuser':u,'form': form,'re':re,},context_instance = RequestContext(request),)

		
@login_required	
def settings(request,user_id):
	u = User.objects.get(id=user_id)
	unread = Mess.objects.filter(receiver=u,unread=True)
	if not u == request.user:
		return HttpResponseRedirect(reverse('messages',args=[request.user.id]))
	# settings
	return render_to_response('profiler/settings.html', {'theuser':u,'unread':unread,},context_instance = RequestContext(request),)
		
