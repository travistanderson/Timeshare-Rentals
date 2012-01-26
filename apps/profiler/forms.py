# profiler/forms.py
from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.db.models import get_model
from django.forms.extras import widgets
from django.utils.translation import ugettext_lazy as _
from profiler.models import Mess


class LoginForm(forms.Form):
	username = forms.CharField(max_length=30,label='Username')
	password = forms.CharField(max_length=100,label='Password',widget=forms.PasswordInput)


class NewUserForm(forms.ModelForm):
	"""
	A form that creates a user, with no privileges, from the given username, email and password.
	"""
	username = forms.RegexField(label=_("Username"), max_length=30, regex=r'^\w+$',
		help_text = _("Required. 30 characters or fewer. Alphanumeric characters only (letters, digits and underscores)."),
		error_message = _("This value must contain only letters, numbers and underscores."))
	email = forms.EmailField(label=_("Email"),)
	password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
	password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ("username",)

	def clean_username(self):
		username = self.cleaned_data["username"]
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError(_("A user with that username already exists."))

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1", "")
		password2 = self.cleaned_data["password2"]
		if password1 != password2:
			raise forms.ValidationError(_("The two password fields didn't match."))
		return password2

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user
		
		
class MessForm(forms.ModelForm):
	# name = forms.CharField(widget=forms.TextInput(attrs={'size':'35'}))
	# description = forms.CharField(widget=forms.Textarea(attrs={'cols':'50'}))
	# addedresortname = forms.CharField(widget=forms.TextInput(attrs={'size':'35'}),label='Name of Resort',required=False)
	# start_room = forms.CharField(widget=forms.TextInput(attrs={'size':'8'}),label='Start Date')
	# end_room = forms.CharField(widget=forms.TextInput(attrs={'size':'8'}),label='End Date')
		
	class Meta:
		model = Mess
		exclude = ('unread','sender','receiver','replied','name','email',)

	def __init__(self, where, *args, **kwargs):
		super(MessForm, self).__init__(*args, **kwargs)
		if where == 0:
			self.fields['namer'] = forms.CharField(label='Name',help_text='htn',required=True,)
			self.fields['emailer'] = forms.EmailField(label='Email',help_text='hte',required=True,)



# 
# 
# 
# 	
# class LoginForm(forms.Form):
# 	username = forms.CharField(max_length=30,label='Username')
# 	password = forms.CharField(max_length=100,label='Password',widget=forms.PasswordInput)
	
	
class ForgotForm(forms.Form):
	email = forms.EmailField()
	
	def clean_email(self):
		data = self.cleaned_data['email']
		allusers = User.objects.all()
		inthere = False
		for auser in allusers:
			if auser.email == data:
				inthere = True
		if inthere == False:
			raise forms.ValidationError('That Email is not in our database')
		return data


class PasswordResetForm(forms.Form):
	new_password_1 = forms.CharField(max_length=16, widget=forms.PasswordInput, required=True,)
	new_password_2 = forms.CharField(max_length=16, widget=forms.PasswordInput, required=True,)
   
	def clean(self):
		cleaned_data = self.cleaned_data
		new_password_1 = cleaned_data.get('new_password_1')
		new_password_2 = cleaned_data.get('new_password_2')
		if new_password_1 and new_password_2:
			if (self.cleaned_data['new_password_1'] != self.cleaned_data['new_password_2']):
				raise forms.ValidationError("You entered two different passwords")
		return self.cleaned_data


class PasswordChangeForm(forms.Form):
	old_password = forms.CharField(max_length=30, widget=forms.PasswordInput, required=True,)
	new_password_1 = forms.CharField(max_length=30, widget=forms.PasswordInput, required=True,label='New Password')
	new_password_2 = forms.CharField(max_length=30, widget=forms.PasswordInput, required=True,label='New Password Again')

	def clean(self):
		cleaned_data = self.cleaned_data
		new_password_1 = cleaned_data.get('new_password_1')
		new_password_2 = cleaned_data.get('new_password_2')
		if new_password_1 and new_password_2:
			if (self.cleaned_data['new_password_1'] != self.cleaned_data['new_password_2']):
				raise forms.ValidationError("New Password and New Password Again did not match.")
		return self.cleaned_data



class EmailChangeForm(forms.Form):
	email = forms.EmailField()

		
		
class UserEditForm(forms.Form):
	# first_name = forms.CharField(max_length=30,label='First Name',required=True,)
	# last_name = forms.CharField(max_length=30,label='Last Name',required=True,)
	email = forms.EmailField(label='Email',required=True,)
	# class Meta:
		# model = get_model('auth', 'user')
		# exclude = ('username','password','is_staff','is_active','is_superuser','last_login','date_joined','groups','user_permissions',)
		
		
		
		
	
