# profiler/forms.py
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _
from profiler.models import Mess


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





	
