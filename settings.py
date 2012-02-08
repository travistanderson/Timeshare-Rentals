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
	MEDIA_ROOT = '/home/travis/timesharerentals.com/media/site_media'
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
	'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
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
	'django.contrib.redirects',
	'django.contrib.admin',
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
	'bunks',
	'profiler',
	'pages',
)

SITE_NAME = "timesharerentals.com"

# NUMPHOTOS = (('free','1'),('bronze','3'),('silver','10'),('gold','10'))
# DAYS = {'free':61,'bronze':183,'silver':365,'gold':10000,}
PHOTATS = ({'emptydict':1,},
	{'name':'Free','namel':'free','numphotos':1,'numdays':61,'dollars':0,'ads':1,'featured':0,'statistics':0,'paypalid':'Z3U8KTPX7M4YU','description':'40 Words',},
	{'name':'Bronze','namel':'bronze','numphotos':3,'numdays':183,'dollars':65,'ads':0,'featured':1,'statistics':1,'paypalid':'MBF7JSC4PLHYE','description':'100 Words',},
	{'name':'Silver','namel':'silver','numphotos':10,'numdays':365,'dollars':100,'ads':0,'featured':1,'statistics':1,'paypalid':'268KUB3QJEK3J','description':'Unlimited Words',},
	{'name':'Gold','namel':'gold','numphotos':10,'numdays':10000,'dollars':200,'ads':0,'featured':1,'statistics':1,'paypalid':'ZQ48W8J3LJZ8N','description':'Unlimited Words',})
# TYPES = {'free':1,'bronze':2,'silver':3,'gold':4,}

# PAYPAL_RECEIVER_EMAIL = "travistanderson@gmail.com"
# PAYPAL_RECEIVER_EMAIL = "service@timesharerentals.com"

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = 'timesharerentalscontact@gmail.com'
EMAIL_HOST_PASSWORD = 'Kcc6v6HchHWYXH'
CONTACT_EMAIL = "timesharerentalscontact@gmail.com"
EMAIL_USE_TLS = True


