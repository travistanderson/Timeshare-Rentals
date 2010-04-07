# contact/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from datetime import datetime, timedelta
from photologue.models import Photo
# from calendarer.models import Calendarer

def contact(request):
	p = Photo.objects.filter(is_public=True)
	
	return render_to_response('contact/contact.html', {"photos":p},
		context_instance = RequestContext(request),
	)

# def travdetail(request, trav_slug):
# 	t = Trav.objects.latest('created')
# 	
# 	return render_to_response('homepage/trav_d.html', {'trav': t,},
# 		context_instance = RequestContext(request),
# 	)