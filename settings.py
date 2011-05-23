"""
Master settings files.

Settings that are specific to each deployment should reside in a
local_settings.py file, which overrides the stuff here. If you don't have
one already, you may create a local_settings.py and copy/paste and change
any of the variables here to there.
"""
import os
from deployment.mediasync_settings import MEDIASYNC, MEDIA_CACHE_BUSTER

DEBUG = True
TEMPLATE_DEBUG = True

ADMINS = (
    #('Your name', 'your.name@spam.com'),
)
MANAGERS = ADMINS

BASE_PATH = os.path.abspath(os.path.split(__file__)[0])

# URL root of the site. Used for things like Intense Debate, that require
# a consistent domain name for tagging. No trailing slash.
URL_ROOT = 'http://creepersremorse.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'gsite.db3'
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be avilable on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(BASE_PATH, 'media')
STATIC_ROOT = MEDIA_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/devmedia/'

# URL of the login form
LOGIN_URL = '/accounts/login/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/amedia/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'SOME_UNIQUE_STR_HERE'

AWS_ACCESS_KEY_ID = 'ENTER_YOUR_OWN'
AWS_SECRET_ACCESS_KEY = 'ENTER_YOUR_OWN'

MEDIASYNC['AWS_KEY'] = AWS_ACCESS_KEY_ID
MEDIASYNC['AWS_SECRET'] = AWS_SECRET_ACCESS_KEY
MEDIASYNC['AWS_BUCKET'] = 'my_site'
MEDIASYNC['SERVE_REMOTE'] = False
MEDIASYNC['EMULATE_COMBO'] = True

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    #'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    #'django.core.context_processors.debug',
    #'django.core.context_processors.media',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_PATH, 'html'),
)

INSTALLED_APPS_DJANGO = (
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    #'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    #'django.contrib.sessions',
)

INSTALLED_APPS_LOCAL = (
    'apps.blog',
    'apps.pages',
)

INSTALLLED_APPS_EXTERNAL = (
    'django_extensions',
    'mediasync',
    'fabtastic',
    'gunicorn',
    'tinymce',
    'south',
)

# End result of the above is the same as a single INSTALLED_APPS.
INSTALLED_APPS = INSTALLED_APPS_DJANGO + INSTALLED_APPS_LOCAL + INSTALLLED_APPS_EXTERNAL

TINYMCE_JS_URL = "/devmedia/js/tiny_mce/tiny_mce.js"
TINYMCE_JS_ROOT = os.path.join(MEDIA_ROOT, "js/tiny_mce")
TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    #'plugins': 'fullpage',
    'relative_urls': False,
    'height': 440,
    'width': 900,
    'force_p_newlines': True,
    'remove_linebreaks': True,
}

"""
Settings that are specific to each instance of the CMS should reside in a
local_settings.py file, which over-rides the stuff here.
"""
try:
    from local_settings import *
except ImportError:
    pass
