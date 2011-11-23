# search/views.py
from django.db.models import Q
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from ts.models import Ad, Resort



def search(request):
	query = request.GET.get('search', '')
	searchpage = True
	if query:
		adqset = (Q(name__icontains=query,premod=True) | Q(description__icontains=query,premod=True))
		adresults = Ad.objects.filter(adqset).distinct()
		

		resortqset = (Q(name__icontains=query,premod=True) | Q(description__icontains=query,premod=True))
		resortresults = Resort.objects.filter(resortqset).distinct()

	else:
		adresults = []
		resortresults = []	
	if len(adresults) + len(resortresults) == 0:
		empty = True
	else:
		empty = False
	return render_to_response("search/search.html", {
		"adresults": adresults,
		"resortresults": resortresults,
		"empty":empty,
		"search":query,
	},context_instance = RequestContext(request),)



