# pages/middleware.py
from pages.views import pager
from django.http import Http404
from django.conf import settings

class PageFallbackMiddleware(object):
	def process_response(self, request, response):
		if response.status_code != 404:
			return response # No need to check for a flatpage for non-404 responses.
		try:
			return pager(request, request.path_info)
		# Return the original response if any errors happened. Because this
		# is a middleware, we can't assume the errors will be caught elsewhere.
		except Http404:
			return response
		except:
			if settings.DEBUG:
				raise
			return response
