# Django settings for timeshare project.
try:
	 from local_settings import WHICH_ENVIRONMENT
except ImportError, exp:
	 WHICH_ENVIRONMENT = 'production'

if WHICH_ENVIRONMENT == 'development':			# Django settings on the local dev server for TSR project.
	DEBUG = True
	TEMPLATE_DEBUG = DEBUG
	TEMPLATE_DIRS = ('/Users/travis/Dropbox/webs_travis/dev_timesharerentals/timeshare/templates',)
	MEDIA_ROOT = '/Users/travis/Dropbox/webs_travis/dev_timesharerentals/timeshare/site_media'
	MEDIA_URL = '/site_media/'
	ADMIN_MEDIA_PREFIX = '/admin_media/'

	DATABASE_ENGINE = 'mysql'
	DATABASE_NAME = 'timeshare'
	DATABASE_USER = 'tsruser'
	DATABASE_PASSWORD = '8AGiXg3Q'
	DATABASE_HOST = '192.168.254.155'
	DATABASE_PORT = ''
	
else:			# WHICH_ENVIRONMENT == 'production'			# Django settings on the server for TSR project.
	DEBUG = False
	TEMPLATE_DEBUG = DEBUG
	TEMPLATE_DIRS = ('/home/travis/timesharerentals.com/timeshare/templates')
	MEDIA_ROOT = '/home/travis/timesharerentals.com/timeshare/media/site_media'
	MEDIA_URL = '/site_media/'
	ADMIN_MEDIA_PREFIX = '/admin_media/'

	DATABASE_ENGINE = 'mysql'
	DATABASE_NAME = 'timeshare'
	DATABASE_USER = 'travisnuser'
	DATABASE_PASSWORD = 'Ot1kHQdgbvVU1X'
	DATABASE_HOST = ''
	DATABASE_PORT = ''


TIME_ZONE = 'US/Eastern'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'qylt*edr7=z*f)67cr9ge5g(pa#ng4fb#z(q!w$1&#a38d_fno'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.app_directories.load_template_source',
	# 'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	# 'pagination.middleware.PaginationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.media',
	'django.core.context_processors.request',
)

ROOT_URLCONF = 'timeshare.urls'

LOGIN_URL = '/profile/login'
LOGIN_REDIRECT_URL = '/'

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.markup',
	'django.contrib.admin',
	# 'django.contrib.admindocs',
	'mailer',
	'pagination',
	'threadedcomments',
	'photologue',
	'photos',
	'gravatar',
	'homepage',
	'ts',
	'widget_tweaks',
	'search',
	# 'paypal.standard.ipn',
)

SITE_NAME = "timesharerentals.com"

NUMPHOTOS = (('free','1'),('bronze','3'),('silver','10'),('gold','10'))
DAYS = {'free':61,'bronze':183,'silver':365,'gold':10000,}
# TYPES = {'free':1,'bronze':2,'silver':3,'gold':4,}

# PAYPAL_RECEIVER_EMAIL = "travistanderson@gmail.com"
# PAYPAL_RECEIVER_EMAIL = "service@timesharerentals.com"
