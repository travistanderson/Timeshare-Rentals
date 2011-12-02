# ts/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template import defaultfilters
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.template import defaultfilters
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from datetime import datetime, timedelta
try:
	import json
except ImportError:
	import simplejson as json
import settings
from ts.models import Ad, Country, Photoo, Resort, ADTYPES
from ts.forms import AdForm, AdPicForm


nphr = "--My resort isn't here. Add a new one."


def _getadtype(adtype):
	for ad in ADTYPES:
		if adtype == ad[1].lower():
			theadtype = ad[0]
	return theadtype


def adlist(request):
	today = datetime.today()
	sort = request.GET.get('sort','chrono')			# sorts = (chrono[standard],name,date,resort,country,price)
	direc = request.GET.get('direc','asc')
	if sort == 'name':
		if direc == 'asc':
			adlist = Ad.objects.filter(premod=True,paid=True,expiration_date__gte=today).order_by('name')
		else:
			adlist = Ad.objects.filter(premod=True,paid=True,expiration_date__gte=today).order_by('-name')	
	elif sort == 'date':
		if direc == 'asc':
			adlist = Ad.objects.filter(premod=True,paid=True,expiration_date__gte=today).order_by('start_room')
		else:
			adlist = Ad.objects.filter(premod=True,paid=True,expiration_date__gte=today).order_by('-start_room')
	elif sort == 'resort':
		if direc == 'asc':
			adlist = Ad.objects.filter(premod=True,paid=True,expiration_date__gte=today).order_by('resort')
		else:
			adlist = Ad.objects.filter(premod=True,paid=True,expiration_date__gte=today).order_by('-resort')
	elif sort == 'country':
		if direc == 'asc':
			adlist = Ad.objects.filter(premod=True,paid=True,expiration_date__gte=today).order_by('resort__address_country')
		else:
			adlist = Ad.objects.filter(premod=True,paid=True,expiration_date__gte=today).order_by('-resort__address_country')
	elif sort == 'price':
		if direc == 'asc':
			adlist = Ad.objects.filter(premod=True,paid=True,expiration_date__gte=today).order_by('price')
		else:
			adlist = Ad.objects.filter(premod=True,paid=True,expiration_date__gte=today).order_by('-price')			
	else: # this is the chrono[standard]
		adlist = Ad.objects.filter(premod=True,paid=True,expiration_date__gte=today).order_by('-adtype')
		
	p = Paginator(adlist,8)
	try:
		page = int(request.GET.get('page','1'))
	except ValueError:
		page = 1
	try:
		ads = p.page(page)
	except (EmptyPage, InvalidPage):
		ads = p.page(p.num_pages)
	return render_to_response('ads/adlist.html', {"ads":ads,'sort':sort,'direc':direc,},context_instance = RequestContext(request),)

	
def addetail(request,ad_id,ad_slug):		
	a = Ad.objects.get(id=ad_id)
	a.paypalid = settings.PHOTATS[a.adtype]['paypalid']
	user = request.user
	if a.expiration_date < datetime.now().date():
		a.expired = True
	return render_to_response('ads/addetail.html', {'ad':a,'user':user},context_instance = RequestContext(request),)


def resortlist(request):
	today = datetime.today()
	sort = request.GET.get('sort','chrono')			# sorts = (chrono[standard],name,date,resort,country)
	direc = request.GET.get('direc','asc')
	if sort == 'country':
		if direc == 'asc':
			rlist = Resort.objects.filter(premod=True).exclude(name=nphr).order_by('address_country')
		else:
			rlist = Resort.objects.filter(premod=True).exclude(name=nphr).order_by('-address_country')
	else: # this is the chrono[standard]
		rlist = Resort.objects.filter(premod=True).exclude(name=nphr).order_by('name')
	for resort in rlist:
		resort.ads = Ad.objects.filter(resort=resort,paid=True,premod=True)
	p = Paginator(rlist,8)
	try:
		page = int(request.GET.get('page','1'))
	except ValueError:
		page = 1
	try:
		resorts = p.page(page)
	except (EmptyPage, InvalidPage):
		resorts = p.page(p.num_pages)
	return render_to_response('resorts/resortlist.html', {"resorts":resorts,'sort':sort,'direc':direc,},context_instance = RequestContext(request),)

	
def resortdetail(request,resort_slug):		
	r = Resort.objects.get(slug=resort_slug)
	r.ads = Ad.objects.filter(resort=r,paid=True,premod=True)
	return render_to_response('resorts/resort.html', {'resort':r,},context_instance = RequestContext(request),)



def chart(request):
	return render_to_response('create/chart.html', context_instance = RequestContext(request),)


@login_required
def newadcreate(request, adtype):
	if request.method == 'POST':
		form = AdForm(request.POST)
		if form.is_valid():
			adform = form.save(commit=False)
			adform.start_ad = datetime.now()
			adform.creator = request.user
			adform.premod = False
			if adtype == 'free':
				adform.paid = True
			else:
				adform.paid = False
			adform.adtype = _getadtype(adtype)
			adform.expiration_date = datetime.now() + timedelta(days=settings.PHOTATS[adform.adtype]['numdays'])
			adform.slug = defaultfilters.slugify(adform.name)
			adform.save()
			if str(form.cleaned_data['resort']) == nphr:
				if form.cleaned_data['addedresortname'] != '':
					newresort = Resort()
					newresort.name = form.cleaned_data['addedresortname']
					newresort.save()
					adform.resort = newresort
					adform.save()
			a = Ad.objects.get(id=adform.id)
			return HttpResponseRedirect(reverse('createpictures', args=[str(a.id)]))		# ? choice page
		else:
			form = AdForm(request.POST)
		return render_to_response('create/newadcreate.html',{'form':form,'adtype':adtype,}, context_instance = RequestContext(request),)
	else:
		form = AdForm()
	return render_to_response('create/newadcreate.html',{'form':form,'adtype':adtype,}, context_instance = RequestContext(request),)
	

@login_required
def adedit(request,ad_id): 
	ad = get_object_or_404(Ad,id=ad_id)
	if not request.user == ad.creator:	# check to make sure only the owner can edit
		return HttpResponseRedirect(reverse('home'))
	adtype = ad.get_adtype_display()
	if request.method == 'POST':
		form = AdForm(request.POST,instance=ad)
		if form.is_valid():
			# handle html cleaning here
			if str(form.cleaned_data['resort']) == nphr:
				if form.cleaned_data['addedresortname'] != '':
					newresort = Resort()
					newresort.name = form.cleaned_data['addedresortname']
					newresort.save()
			form.save()
			# return HttpResponseRedirect('/ads/create-add-pictures/%s/' %(str(ad.id)))
			return HttpResponseRedirect(reverse('profile', args=[str(request.user.id)]))		# ? choice page
		else:
			form = AdForm(request.POST,instance=ad)
		return render_to_response('create/newadcreate.html', {'form': form,'adtype':adtype,}, context_instance = RequestContext(request),)
	else:
		form = AdForm(instance=ad)
	return render_to_response('create/newadcreate.html', {'form': form,'adtype':adtype,}, context_instance = RequestContext(request),)

@login_required
def addelete(request,ad_id):
	ad = get_object_or_404(Ad,id=ad_id)
	user = request.user
	if not user == ad.creator:	# check to make sure only the owner can edit
		return HttpResponseRedirect(reverse('home'))
	if request.method == 'POST':
		ad.delete()
		return HttpResponseRedirect(reverse('profile', args=[str(user.id)]))
	return render_to_response('ads/addelete.html', {'ad':ad,}, context_instance = RequestContext(request),)


def _photosquasher(ad):		# This is a helper for reordering the photos - take all the gaps out of numbering
	photos = ad.photos.all().order_by('orderer')
	for c, photo in enumerate(photos):
		photo.orderer = c + 1
		photo.save()


@login_required	
def createpictures(request,ad_id):
	ad = Ad.objects.get(id=ad_id)
	user = request.user
	if not user == ad.creator:	# check to make sure only the owner can edit
		return HttpResponseRedirect(reverse('home'))
	ad.canaddmore = True
	maxer = int(settings.PHOTATS[ad.adtype]['numphotos'])
	if len(ad.photos.all()) >= maxer:
		ad.canaddmore = False
	if ad.canaddmore:
		ad.howmanymore = maxer - len(ad.photos.all())
	if request.method == 'POST':
		form = AdPicForm(ad,request.POST, request.FILES)
		if form.is_valid():
			new_pic = form.save(commit=False)
			new_pic.title = str(request.user.username) + ' ' + ad.name[0:10] + ' ' + str(datetime.now().strftime("%y%m%d%H%M%S"))
			new_pic.title_slug = defaultfilters.slugify(new_pic.title)
			new_pic.orderer = ad.photos.all().count() + 1
			new_pic.save()
			ad.photos.add(new_pic)
			ad.save()
			if form.cleaned_data['deleter']:
				pho = Photoo.objects.get(id=form.cleaned_data['deleter'].id)
				pho.delete()
				_photosquasher(ad)
			if len(ad.photos.all()) > maxer:
				pho = Photoo.objects.latest('orderer')
				pho.delete()
				_photosquasher(ad)
			return HttpResponseRedirect(reverse('createpictures', args=[str(ad.id)])) # payment page
	else:
		form = AdPicForm(ad)
	return render_to_response('create/add_pictures.html', {'form': form,'ad':ad,}, context_instance = RequestContext(request),)


@login_required
def photorder(request,ad_id):# check to make sure only the owner can edit
	orar = request.GET.get('order','')
	orar = orar.split(',')
	orar2 = []
	for thing in orar:
		orar2.append(int(thing.split('-')[1]))
	ad = Ad.objects.get(id=ad_id)
	c = 0
	for photo in ad.photos.all().order_by('orderer'):
		d = 0
		for num in orar2:
			if photo.orderer == orar2[d]:
				photo.orderer = d + 1
				photo.save()	
				break
			d += 1	
		c +=1
	if request.is_ajax():
		info = {}
		info['worked'] = 'success'
		data = json.dumps(info)
		return HttpResponse(data,mimetype='application/javascript')
	
	return render_to_response('create/add_pictures.html',{'ad':ad,'phtc':phtc},context_instance = RequestContext(request),)



@login_required
def paysuccess(request):
	return render_to_response('ads/paysuccess.html', context_instance = RequestContext(request),)



@login_required
def paycancel(request):
	return render_to_response('ads/paycancel.html', context_instance = RequestContext(request),)



# @permission_required('ts.view_paypal')
def paypal(request):
	return render_to_response('ads/paypal.html', context_instance = RequestContext(request),)	



# TODO make a choice page where it asks about payment, creating another ad




