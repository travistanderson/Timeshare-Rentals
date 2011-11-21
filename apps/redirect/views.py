# redirect/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
# from django.core.urlresolvers import reverse
from django.template import RequestContext
from redirect.models import Redirector



def redirecturl(request,old_url):
	# u = get_object_or_404(Redirector,oldurl=old_url)

	return render_to_response('redirector.html', {"u":old_url,},context_instance = RequestContext(request),)
	# return redirect(u.newurl)



