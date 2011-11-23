# pages/views.py
from pages.models import Page
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.core.xheaders import populate_xheaders
from django.utils.safestring import mark_safe

DEFAULT_TEMPLATE = 'pages/default.html'

def pager(request, url):
	"""
	Page view.

	Models: `pages.Page`
	Templates: Uses the template defined by the ``template_name`` field,
		or `pages/default.html` if template_name is not defined.
	Context:
		page
			`pages.pages` object
	"""
	if not url.endswith('/') and settings.APPEND_SLASH:
		return HttpResponseRedirect("%s/" % request.path)
	if not url.startswith('/'):
		url = "/" + url
		
	ptest = Page.objects.get(url=url)
	if ptest.active:
		p = get_object_or_404(Page, url__exact=url)
	else:
		p = get_object_or_404(Page, url__exact="/doesn't-exist/")

	# ta = Tininav.objects.all()
	# theone = False
	# for tn in ta:
	# 	for page in tn.pages.all():
	# 		if page.id == p.id:
	# 			theone = tn.id
	# 			break				
	# tn = ''
	# if theone:			
	# 	tn = Tininav.objects.get(id=theone)
	# 	r = []
	# 	for j in tn.pages.all():
	# 		t1 = [j.url,j.title]
	# 		r.append(t1)
	# else:
	# 	r =[]
		
	# s = [['/here/','Here'],['/there/','There'],['/everywhere/','Everywhere']]

	if p.templatr:
		t = loader.select_template((p.templatr, DEFAULT_TEMPLATE))
	else:
		t = loader.get_template(DEFAULT_TEMPLATE)

	# To avoid having to always use the "|safe" filter in flatpage templates,
	# mark the title and content as already safe (since they are raw HTML
	# content in the first place).
	p.title = mark_safe(p.title)
	p.content = mark_safe(p.content)

	c = RequestContext(request, {'pager': p,})
	response = HttpResponse(t.render(c))
	populate_xheaders(request, response, Page, p.id)
	return response

	
def video(request, name):
	v = name
	
	return render_to_response('pages/video.html', {'name': v,},
		context_instance = RequestContext(request),
	)
