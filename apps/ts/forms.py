# ts/forms.py
from django import forms
from django.contrib.admin import widgets
from datetime import datetime, timedelta
from ts.models import Ad, Country, Resort, ResortType
from ts.widgets import Dateranger
from photologue.models import Photo

class PremiumForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'size':'35'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'cols':'50'}))
	start_room = forms.CharField(widget=forms.TextInput(attrs={'size':'8'}))
	end_room = forms.CharField(widget=forms.TextInput(attrs={'size':'8'}))
	add_resort = forms.CharField(widget=forms.CheckboxInput(attrs={'id':'add_resort'}))
    
	class Meta:
		model = Ad
		exclude = ('creator','premium','premod',)
     
    # def __init__(self, user=None, *args, **kwargs):
    #     self.user = user
    #     super(PhotoUploadForm, self).__init__(*args, **kwargs)

class FreeForm(forms.ModelForm):
	
	name = forms.CharField(widget=forms.TextInput(attrs={'size':'35'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'cols':'50'}))
	start_room = forms.CharField(widget=forms.TextInput(attrs={'size':'8'}))
	end_room = forms.CharField(widget=forms.TextInput(attrs={'size':'8'}))
	add_resort = forms.CharField(widget=forms.CheckboxInput(attrs={'id':'add_resort'}))
	
    
	class Meta:
		model = Ad
		exclude = ('creator','duration','premium','premod',)
        
    # def __init__(self, user=None, *args, **kwargs):
    #     self.user = user
    #     super(PhotoEditForm, self).__init__(*args, **kwargs)


class AdPicForm(forms.ModelForm):

	caption = forms.CharField(widget=forms.Textarea(attrs={'cols':'30','rows':'3'}))
	class Meta:
		model = Photo
		exclude = ('title_slug','date_added','tags','is_public','crop_from','effect','title',)



class GenericForm(forms.ModelForm):
	class Meta:
		model = Photo
		exclude = ('title','title_slug','date_added','tags','is_public','crop_from','effect',)



class ResortForm(forms.ModelForm):
	# name = forms.CharField(widget=forms.Select(attrs={'id':'id_resort'}))
	# add_resort = forms.CharField(widget=forms.CheckboxInput(attrs={'id':'add_resort'}))
	# new_resort_name = forms.CharField()
	class Meta:
		model = Resort
		exclude = ('premod','comment','address','email','picture','description','url',)




class ResortTypeForm(forms.ModelForm):
	class Meta:
		model = ResortType



class CounrtyForm(forms.ModelForm):
	class Meta:
		model = Country
		exclude = ('iso','iso3','flag',)



