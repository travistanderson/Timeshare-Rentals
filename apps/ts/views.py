# ts/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template import defaultfilters
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import settings
# from photologue.models import Photo, Gallery
from ts.models import Ad, Country, Photoo, Resort
from ts.forms import AdPicForm, EditAdForm, NewAdForm


def adlist(request):
	ap = Ad.objects.filter(adtype__gt=1, premod=True)
	af = Ad.objects.filter(adtype__lt=2, premod=True)
	return render_to_response('ads/adlist.html', {"adp_list":ap,"adf_list":af,},context_instance = RequestContext(request),)

	
def addetail(request,ad_id):		
	a = Ad.objects.get(id=ad_id)
	if a.expiration_date < datetime.now().date():
		a = None
	return render_to_response('ads/addetail.html', {'ad':a,},context_instance = RequestContext(request),)


def chart(request):
	return render_to_response('create/chart.html', context_instance = RequestContext(request),)


@login_required
def newadcreate(request, adtype):
	if request.method == 'POST':
		form = NewAdForm(request.POST)
		if form.is_valid():
			adform = form.save(commit=False)
			adform.start_ad = datetime.now()
			adform.creator = request.user
			adform.premod = False
			adform.expiration_date = datetime.now() + timedelta(days=settings.DAYS[adtype])
			adform.adtype = ad.get_adtype_display()
			adform.save()
			if str(form.cleaned_data['resort']) == "My resort isn't here. Add a new one.":
				if form.cleaned_data['addedresortname'] != '':
					newresort = Resort()
					newresort.name = form.cleaned_data['addedresortname']
					newresort.save()
					adform.resort = newresort
					adform.save()
			a = Ad.objects.get(id=adform.id)
			return HttpResponseRedirect(reverse('createpictures', args=[str(a.id)]))		# ? choice page
		else:
			form = NewAdForm(request.POST)
		return render_to_response('create/newadcreate.html',{'form':form,'adtype':adtype,}, context_instance = RequestContext(request),)
	else:
		form = NewAdForm()
	return render_to_response('create/newadcreate.html',{'form':form,'adtype':adtype,}, context_instance = RequestContext(request),)
	

@login_required
def adedit(request,ad_id):
	ad = get_object_or_404(Ad,id=ad_id)
	adtype = ad.get_adtype_display()
	if request.method == 'POST':
		form = EditAdForm(request.POST,instance=ad)
		if form.is_valid():
			if str(form.cleaned_data['resort']) == "My resort isn't here. Add a new one.":
				if form.cleaned_data['addedresortname'] != '':
					newresort = Resort()
					newresort.name = form.cleaned_data['addedresortname']
					newresort.save()
			form.save()
			# return HttpResponseRedirect('/ads/create-add-pictures/%s/' %(str(ad.id)))
			return HttpResponseRedirect(reverse('createpictures', args=[str(ad.id)]))		# ? choice page
		else:
			form = EditAdForm(request.POST,instance=ad)
		return render_to_response('create/newadcreate.html', {'form': form,'adtype':adtype,}, context_instance = RequestContext(request),)
	else:
		form = EditAdForm(instance=ad)
	return render_to_response('create/newadcreate.html', {'form': form,'adtype':adtype,}, context_instance = RequestContext(request),)
		

@login_required	
def createpictures(request,ad_id):
	ad = Ad.objects.get(id=ad_id)
	# ph = ad.photos.all()
	# if len(ph) >= int(settings.NUMPHOTOS[ad.adtype-1][1]):
	# 	print "make the user pic a photo to delete"
	# else:
	if request.method == 'POST':
		form = AdPicForm(ad,request.POST, request.FILES)
		if form.is_valid():
			new_pic = form.save(commit=False)
			new_pic.title = str(request.user.username) + ' ' + ad.name + ' ' + str(datetime.now().strftime("%y-%m-%d %H:%M"))
			new_pic.title_slug = defaultfilters.slugify(new_pic.title)
			new_pic.orderer = ad.photos.all().count() + 1
			new_pic.save()
			ad.photos.add(new_pic)
			ad.save()
			return HttpResponseRedirect('/') # payment page
	else:
		form = AdPicForm(ad)
	return render_to_response('create/add_pictures.html', {'form': form,'ad':ad,}, context_instance = RequestContext(request),)


	
# TODO make a choice page where it asks about payment, adding more pictures, creating another ad
# TODO ad reordering photos to editad view, adding more pictures, picking the one to delete before adding a new one
# TODO ad picking the one to delete before adding a new one to the create pictures view


