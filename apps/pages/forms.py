# pages/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from pages.widgets import travEditor, WMDEditor
from pages.models import Page

		
class PageAdminModelForm(forms.ModelForm):
	content = forms.CharField(widget=travEditor())
	url = forms.RegexField(label="URL", max_length=100, regex=r'^[-\w/]+$',
		help_text ="Example: '/about/contact/'. Make sure to have leading"
						" and trailing slashes.",
		error_message ="This value must contain only letters, numbers,"
						" underscores, dashes or slashes.")

	class Meta:
		model = get_model('pages', 'page')

class PageBrickAdminModelForm(forms.ModelForm):
	content = forms.CharField(widget=WMDEditor())