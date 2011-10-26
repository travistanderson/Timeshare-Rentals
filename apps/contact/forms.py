# contact/forms.py
from django import forms
from django.forms.models import ModelForm
from django.contrib.admin.widgets import FilteredSelectMultiple

class ContactForm(forms.Form):
	name = forms.CharField(max_length=100,label='Name')
	email = forms.EmailField(label='Email Address')
	subject = forms.CharField(max_length=100,label='Topic')
	content = forms.CharField(widget=forms.Textarea,label='Comments')
