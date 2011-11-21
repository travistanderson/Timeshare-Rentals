from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.contrib import admin

import os.path

admin.autodiscover()

urlpatterns = patterns('',
	(r'^ads/', include('ts.urls')),
	(r'^calendar/', include('calendarer.urls')),
	(r'^contact/', include('contact.urls')),	
	(r'^profile/', include('profiler.urls')),
	(r'^photologue/', include('photologue.urls')),
	(r'^search/', include('search.urls')),
	(r'^$', include('homepage.urls')),
    # (r'^admin/', include('admints.urls')),
	(r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^my_admin/jsi18n', 'django.views.i18n.javascript_catalog'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(__file__), "site_media")}),
    )