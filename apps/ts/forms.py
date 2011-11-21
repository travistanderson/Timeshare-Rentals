# ts/forms.py
from django import forms
from django.contrib.admin import widgets
from datetime import datetime, timedelta
import settings
from ts.models import Ad, Country, Photoo, Resort
from ts.widgets import Dateranger



class NewAdForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'size':'35'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'cols':'50'}))
	addedresortname = forms.CharField(widget=forms.TextInput(attrs={'size':'35'}),label='Name of Resort',required=False)
	start_room = forms.CharField(widget=forms.TextInput(attrs={'size':'8'}),label='Start Date')
	end_room = forms.CharField(widget=forms.TextInput(attrs={'size':'8'}),label='End Date')
	price = forms.CharField(widget=forms.TextInput(attrs={'size':'8'}),label='Price')
		
	class Meta:
		model = Ad
		exclude = ('creator','adtype','premod','photos','expiration_date')
		fields = ('name','description','resort','addedresortname','start_room','end_room','price',)

	 
class EditAdForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'size':'35'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'cols':'50'}))
	addedresortname = forms.CharField(widget=forms.TextInput(attrs={'size':'35'}),label='Name of Resort',required=False)
	start_room = forms.CharField(widget=forms.TextInput(attrs={'size':'8'}),label='Start Date')
	end_room = forms.CharField(widget=forms.TextInput(attrs={'size':'8'}),label='End Date')
	price = forms.CharField(widget=forms.TextInput(attrs={'size':'8'}),label='Price')
		
	class Meta:
		model = Ad
		exclude = ('creator','adtype','premod','photos','expiration_date')
		fields = ('name','description','resort','addedresortname','start_room','end_room','price',)


class AdPicForm(forms.ModelForm):
	caption = forms.CharField(widget=forms.Textarea(attrs={'cols':'30','rows':'3'}))
	# deleter = forms.ModelChoiceField(queryset=Photoo.objects.all(),empty_label=None,required=False)
	class Meta:
		model = Photoo
		exclude = ('title_slug','date_added','tags','is_public','crop_from','effect','title','orderer')
	def __init__(self, ad, *args, **kwargs):
		super(AdPicForm, self).__init__(*args, **kwargs)
		mypics = ad.photos.all()
		# if int(mypics.count()) >= int(settings.NUMPHOTOS[ad.adtype-1][1]):
		self.fields['deleter'] = forms.ModelChoiceField(queryset=mypics,label='Select photo to delete.',required=False,)




