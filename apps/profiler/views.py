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
import settings
from profiler.models import Mess, EmailReset
from profiler.forms import EmailChangeForm, ForgotForm, LoginForm, MessForm, NewUserForm, PasswordChangeForm, PasswordResetForm, UserEditForm
from photologue.models import Photo, Gallery
from ts.models import Ad, Resort
from mailer import send_mail

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


# def logout_view(request):
# 	logout(request)
# 	return HttpResponseRedirect(reverse('home'))


	
def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect('/')
				else:
					#disable account error message
					message = 'your account is disabled'
			else:
				form = LoginForm(request.POST)
				# signupform = SignupForm()
				message = 'Your username and password did not match. Please try again.'
				return render_to_response('profiler/login.html',{'loginform':form,'message':message,},context_instance = RequestContext(request),)
		else:
			form = LoginForm(request.POST)
			# signupform = SignupForm()
			return render_to_response('profiler/login.html',{'loginform':form,},context_instance = RequestContext(request),)
	else:
		form = LoginForm()
		# signupform = SignupForm()
	return render_to_response('profiler/login.html', {'loginform':form,}, context_instance = RequestContext(request),)	




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
	for ad in ads:
		# ad.paypalid = settings.SITE_NAME
		ad.paypalid = settings.PHOTATS[ad.adtype]['paypalid']
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
def usersettings(request,user_id):
	u = User.objects.get(id=user_id)
	unread = Mess.objects.filter(receiver=u,unread=True)
	if not u == request.user:
		return HttpResponseRedirect(reverse('messages',args=[request.user.id]))
	# settings
	return render_to_response('profiler/settings.html', {'theuser':u,'unread':unread,},context_instance = RequestContext(request),)
		



# =======

	
def forgot_view(request):
	if request.method == 'POST':
		form = ForgotForm(request.POST)
		if form.is_valid():
			theemail = form.cleaned_data['email']
			user = get_object_or_404(User, email=theemail)
			reset = EmailReset()
			reset.email = theemail
			reset.expires = datetime.now() + timedelta(hours=2)
			thekey = hashlib.sha1()
			thekey.update(str(reset.expires)+str('gobledeegook45'))
			reset.key = thekey.hexdigest()
			reset.save()
			
			subject = 'TimeshareRentals.com Password Reset Notification'
			toemail = ['travistanderson@gmail.com','modernarrangements@gmail.com',theemail]
			fromemail = settings.CONTACT_EMAIL
			content = '''
%s,

Here is your password reset link, http://timesharerentals.com/profile/password-reset/%s/  
Use it to reset your password. This link will be valid until %s Eastern time. After that you will have to click the forgot password link again and get a new reset email.

If you did not fill out the forgot password form and suspect that someone else is trying to reset your password please contact us at timesharerentalscontact@gmail.com.

TimeshareRentals.com
			
			
			''' %(user.first_name,reset.key,reset.expires.strftime('%a, %d %b %Y %I:%M %p'))
			
			send_mail(subject,content,fromemail,toemail)
			return HttpResponseRedirect(reverse('forgot_submit'))
		else:
			form = ForgotForm(request.POST)
			return render_to_response('profiler/forgot.html',{'forgotform':form,},context_instance = RequestContext(request),)
	else:
		form = ForgotForm()
	return render_to_response('profiler/forgot.html', {'forgotform':form,}, context_instance = RequestContext(request),)
	
	
def forgot_submit(request):
	return render_to_response('profiler/forgot_submit.html', context_instance = RequestContext(request),)
	
	

def passwordreset(request,key):
	message = ""
	if request.method == "POST":
		m = "post"
		form = PasswordResetForm(request.POST)
		if form.is_valid():			# this calls some django cleaning and then my custom clean method in forms.py on the ForgotForm class
			try:
				reset = EmailReset.objects.get(key=key)
				now = datetime.now()
				if now < reset.expires:
					email = reset.email
					user = get_object_or_404(User, email=email)
					password = form.cleaned_data['new_password_1']
					user.set_password(password)
					user.save()
					return HttpResponseRedirect(reverse('passwordreset_submit'))
				else:
					message = "The reset has expired. Please return to the <a href='%s'>forgot password</a> page and get a new reset." %(reverse('forgot_view'))
					# return HttpResponseRedirect(reverse('forgot_view'))
			except EmailReset.DoesNotExist:
				message = 'That email address is not assigned to any users.'
	else:		# user did not click submit button or it was the first time the page was loaded
		form = PasswordResetForm()
		m = "get"
	return render_to_response('profiler/passwordreset.html',{'form':form,'message':message,'key':key,},context_instance = RequestContext(request),)



def passwordreset_submit(request):
	return render_to_response('profiler/passwordreset_submit.html',context_instance = RequestContext(request),)


	
@login_required
def changepassword(request,username):
	user = request.user
	u = get_object_or_404(User,username=username)
	if user != u:
		return HttpResponseRedirect(reverse('changepassword',args=[user.username,]))
	if request.method == "POST":
		form = PasswordChangeForm(request.POST)
		if form.is_valid():			# this calls some django cleaning and then my custom clean method in forms.py on the ForgotForm class
			old = form.cleaned_data['old_password']
			new = form.cleaned_data['new_password_1']
			if not user.check_password(old):
				message = 'Your old password was enetered incorrectly.'
				return render_to_response('profiler/changepassword.html',{'form':form,'message':message,},context_instance = RequestContext(request),)
			else:
				user.set_password(new)
				user.save()
				return HttpResponseRedirect(reverse('usersettings',args=[user.id]))
		else:		# form was invalid
			# form = PasswordChangeForm(request.POST,user)
			form = PasswordChangeForm(request.POST)
		return render_to_response('profiler/changepassword.html',{'form':form,},context_instance = RequestContext(request),)
	else:		# user did not click submit button or it was the first time the page was loaded
		# form = PasswordChangeForm(user)
		form = PasswordChangeForm()
	return render_to_response('profiler/changepassword.html',{'form':form,},context_instance = RequestContext(request),)



	
@login_required
def changeemail(request,username):
	user = request.user
	u = get_object_or_404(User,username=username)
	if user != u:
		return HttpResponseRedirect(reverse('changeemail',args=[user.username,]))
	if request.method == "POST":
		form = EmailChangeForm(request.POST)
		if form.is_valid():
			u.email = form.cleaned_data['email']
			u.save()
			return HttpResponseRedirect(reverse('usersettings',args=[user.id]))
		else:		# form was invalid
			form = EmailChangeForm(request.POST)
		return render_to_response('profiler/changeemail.html',{'form':form,},context_instance = RequestContext(request),)
	else:		# user did not click submit button or it was the first time the page was loaded
		form = EmailChangeForm()
	return render_to_response('profiler/changeemail.html',{'form':form,},context_instance = RequestContext(request),)	
	
	
	
	
	