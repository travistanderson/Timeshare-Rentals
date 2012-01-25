# homepage/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from datetime import datetime, timedelta
from photologue.models import Photo
from ts.models import Resort, Ad

def home(request):
	today = datetime.today()
	ap = Ad.objects.filter(adtype__gt=1, premod=True,paid=True,expiration_date__gte=today)
	# maybe add in some kind of randamizer to mix up which ads show
	return render_to_response('homepage/homepage.html', {"adp_list":ap,},context_instance = RequestContext(request),)
