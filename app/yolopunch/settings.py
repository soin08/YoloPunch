"""
Django settings for yolopunch project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
YOLO_ROOT = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

#print(os.path.join(BASE_DIR, ".tmp"))
#print(os.path.join(YOLO_ROOT, ".tmp"))
#print(os.path.abspath(os.path.dirname(os.path.dirname(BASE_DIR))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*oyrr3hd3l+g(u1mphx*898+6*34x$o#y#x2teu0%()^$h!r#&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = [ os.path.join(BASE_DIR, 'templates') ]

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'rest_framework',
    'yolo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'yolopunch.urls'

WSGI_APPLICATION = 'yolopunch.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': 'soinrocks',
        #'USER' : 'soin08',
        #'PASSWORD' : '1September',
        #'HOST' : '127.0.0.1',
        #'PORT' : '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = False # Automatically log the user in.
REGISTRATION_OPEN = True
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
   'django.contrib.staticfiles.finders.FileSystemFinder',
   'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_ROOT = ''

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(YOLO_ROOT, ".tmp"),
)

MEDIA_ROOT =  os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

