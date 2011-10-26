# admints/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template import defaultfilters
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from photologue.models import Photo, Gallery
from ts.models import Ad, Comment, Resort, ResortType



@login_required	
def adminindex(request):		
	a = Ad.objects.filter(premod=False)
	c = Comment.objects.filter(premod=False)
	r = Resort.objects.filter(premod=False)
	rt = ResortType.objects.filter(premod=False)
		
	return render_to_response('admin/admints/index.html', {"ads":a,'comments':c,'resorts':r,'resorttypes':rt,},
		context_instance = RequestContext(request),
	)
