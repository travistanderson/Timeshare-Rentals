# calendarer/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from datetime import datetime, timedelta
from photologue.models import Photo
# from calendarer.models import Calendarer

def calendar(request):
	p = Photo.objects.filter(is_public=True)
	return render_to_response('calendar/calendar.html', {"photos":p},context_instance = RequestContext(request),)


