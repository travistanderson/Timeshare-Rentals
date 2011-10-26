# homepage/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from datetime import datetime, timedelta
from photologue.models import Photo
from ts.models import Resort, Ad

def home(request):
	ap = Ad.objects.filter(adtype__gt=1, premod=True)
	return render_to_response('homepage/homepage.html', {"adp_list":ap},context_instance = RequestContext(request),)
