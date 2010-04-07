# profiler/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template import defaultfilters
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from photologue.models import Photo, Gallery
from ts.models import Ad, PhotoOrder, Resort
from ts.forms import AdPicForm, FreeForm, PremiumForm, ResortForm, ResortTypeForm, GenericForm


def proindex(request):
	# ap = Ad.objects.filter(premium=True, premod=True)
	# af = Ad.objects.filter(premium=False, premod=True)
	u = User.objects.all()
	
	return render_to_response('profiler/index.html', {'users':u,},
		context_instance = RequestContext(request),
	)


@login_required	
def profile(request,user_id):		
	u = User.objects.get(id=user_id)
	myp = Ad.objects.filter(premium=True, creator=u, premod=True)
	myf = Ad.objects.filter(premium=False, creator=u, premod=True)
	
	premyp = Ad.objects.filter(premium=True, creator=u, premod=False)
	premyf = Ad.objects.filter(premium=False, creator=u, premod=False)
		
	return render_to_response('profiler/profile.html', {"theuser":u,'mypads':myp,'myfads':myf,'premypads':premyp,'premyfads':premyf,},
		context_instance = RequestContext(request),
	)
