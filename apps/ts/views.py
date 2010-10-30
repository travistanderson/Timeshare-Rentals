# ts/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template import defaultfilters
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from photologue.models import Photo, Gallery
from ts.models import Ad, PhotoOrder, Resort, ResortType
from ts.forms import AdPicForm, CounrtyForm, FreeForm, GenericForm, PremiumForm, ResortForm, ResortTypeForm


def adlist(request):
	ap = Ad.objects.filter(premium=True, premod=True)
	af = Ad.objects.filter(premium=False, premod=True)
	
	return render_to_response('ads/adlist.html', {"adp_list":ap,"adf_list":af,},context_instance = RequestContext(request),)

	
def addetail(request,ad_id):		
	a = Ad.objects.get(id=ad_id)
	u = User.objects.get(id=a.creator.id)
	return render_to_response('ads/addetail.html', {'ad':a,'user':u,},context_instance = RequestContext(request),)



def adedit(request,ad_id):		
	a = Ad.objects.get(id=ad_id)
	u = User.objects.get(id=a.creator.id)
	return render_to_response('ads/adedit.html', {'ad':a,'user':u,},context_instance = RequestContext(request),)



def chart(request):
	ap = Ad.objects.filter(premium=True, premod=True)
	
	return render_to_response('create/chart.html', {"adp_list":ap},
		context_instance = RequestContext(request),
	)


@login_required
def premiumcreate(request):
	if request.method == 'POST':
		form = PremiumForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			duration = form.cleaned_data['duration']
			form_with_now = form.save(commit=False)
			form_with_now.start_ad = datetime.now()
			form_with_now.creator = request.user
			form_with_now.premium = True
			form_with_now.premod = False
			form_with_now.duration = 1

			if form.cleaned_data['add_resort'] == 'on':
				# form_with_now.resort = Resort.objects.get(branch='generic')
				form_with_now.save()
				a = Ad.objects.get(name=name)
				newresort = defaultfilters.slugify(form.cleaned_data['new_resort_name'])
				return HttpResponseRedirect('/ads/create-add-resort-branch/%s/%s/' %(newresort,str(a.id)))
			else:
				form_with_now.resort = form.cleaned_data['resort']
				form_with_now.save()
				a = Ad.objects.get(name=name)
				return HttpResponseRedirect('/ads/create-add-pictures/%s/' %(str(a.id)))

	else:
		form = PremiumForm()
	return render_to_response('create/premium.html', {'form': form,}, context_instance = RequestContext(request),)
	
	
@login_required	
def freecreate(request):
	if request.method == 'POST':
		form = FreeForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			form_with_now = form.save(commit=False)
			form_with_now.start_ad = datetime.now()
			form_with_now.creator = request.user
			form_with_now.premium = False
			form_with_now.premod = False
			form_with_now.duration = 1
			# thetitle = "%s gallery for %s"  %(request.user,form.cleaned_data['name'])
			# theslug =defaultfilters.slugify(thetitle)
			# g = Gallery(title=thetitle,title_slug=theslug)
			# g.save()
			# form_with_now.gallery = g

			if form.cleaned_data['add_resort'] == 'on':
				# form_with_now.resort = Resort.objects.get(branch='generic')
				form_with_now.save()
				a = Ad.objects.get(name=name)
				newresort = defaultfilters.slugify(form.cleaned_data['new_resort_name'])
				return HttpResponseRedirect('/ads/create-add-resort-branch/%s/%s/' %(newresort,str(a.id)))
			else:
				form_with_now.resort = form.cleaned_data['resort']
				form_with_now.save()
				a = Ad.objects.get(name=name)
				return HttpResponseRedirect('/ads/create-add-pictures/%s/' %(str(a.id)))

	else:
		form = FreeForm()
	return render_to_response('create/free.html', {'form': form,}, context_instance = RequestContext(request),)
	

@login_required	
def createpictures(request,ad_id):
	a = Ad.objects.get(id=ad_id)
	ph = a.photos.all()
	if request.method == 'POST':
		form = AdPicForm(request.POST, request.FILES)
		if form.is_valid():
			pos = PhotoOrder.objects.filter(ad=a)
			hm = str(ph.count() + 1)			# this counts how many pictures there are alread and adds one
			caption = form.cleaned_data['caption']
			form_with_now = form.save(commit=False)
			form_with_now.title = str(request.user.username) + ' ' + a.name + ' photo ' + str(hm)
			# title = "someteststring of letters"
			form_with_now.title_slug = defaultfilters.slugify(form_with_now.title)
			form_with_now.save()
			p = Photo.objects.get(title_slug = form_with_now.title_slug)
			a.photos.add(p)
			a.save()
			po = PhotoOrder()
			po.ad = a
			po.photo = p
			po.theorders = hm
			po.save()
			return HttpResponseRedirect('/')
	else:
		form = AdPicForm()
	return render_to_response('create/add_pictures.html', {'form': form,'photos':ph,}, context_instance = RequestContext(request),)
	
	
	# 
	# name = models.ForeignKey(ResortType, blank=True, null=True)
	# branch = models.CharField(max_length=200)
	# description = models.TextField()	
	# picture = models.ForeignKey(Photo, blank=True, null=True)
	# email = models.EmailField(blank=True,)
	# url = models.URLField(blank=True,)
	# address = models.CharField(max_length=200, blank=True,)
	# address_country = models.ForeignKey(Country)



	
@login_required	
def createnewresortbranch(request,newresort,ad_id):
	if request.method == 'POST':
		form = ResortForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			branch = form.cleaned_data['branch']
			address_country = form.cleaned_data['address_country']
			form.save()
			r = Resort.objects.get(name=name)
			a = Ad.objects.get(id=ad_id)
			a.resort = r
			a.save()
			return HttpResponseRedirect('/ads/create-add-pictures/%s/' %(ad_id))
		else:
			return render_to_response('create/add_resort_branch.html', {'form': form,'newresort':newresort,'ad_id':ad_id,}, context_instance = RequestContext(request),)
	else:
		form = ResortForm(initial={'branch':newresort,})
		# form.branch = 'test'
		return render_to_response('create/add_resort_branch.html', {'form': form,'newresort':newresort,'ad_id':ad_id,}, context_instance = RequestContext(request),)




@login_required	
def createnewresort(request,newresort,ad_id):
	if request.method == 'POST':
		form = ResortTypeForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			form.save()
			return HttpResponseRedirect('/ads/create-add-resort-branch/%s/%s/' %(newresort,ad_id))
		else:
			form = ResortTypeForm()
			return render_to_response('create/add_resort.html', {'form': form,'ad_id':ad_id,}, context_instance = RequestContext(request),)
	else:
		form = ResortTypeForm()
		return render_to_response('create/add_resort.html', {'form': form,'ad_id':ad_id,}, context_instance = RequestContext(request),)




@login_required	
def createnewcountry(request,newresort,ad_id):
	if request.method == 'POST':
		form = CounrtyForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			iso = str(name[0:1])
			form.save()
			return HttpResponseRedirect('/ads/create-add-resort-branch/%s/%s/' %(newresort,ad_id))
		else:
			form = CounrtyForm()
			return render_to_response('create/add_country.html', {'form': form,'ad_id':ad_id,}, context_instance = RequestContext(request),)
	else:
		form = CounrtyForm()
		return render_to_response('create/add_country.html', {'form': form,'ad_id':ad_id,}, context_instance = RequestContext(request),)


# name = mode
# branch = mo
# description
# picture = m
# email = mod
# url = model
# address = m
# address_country
# premod = mo
# comment = m