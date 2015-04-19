"""
Django settings for edisco project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!nxsre9j#1o$&#_n7=5s2!1u-j!rx_a$9klg(*5oznb6y!d-$b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'assessmentgenerator',
    'registration',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'edisco.urls'

WSGI_APPLICATION = 'edisco.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

config_path = os.path.dirname(os.path.abspath(__file__))+'/edisco.ini'
from ConfigParser import RawConfigParser
config = RawConfigParser()
config.read(config_path)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config.get('database','DATABASE_NAME'),
        'USER': config.get('database','DATABASE_USER'),
        'PASSWORD': config.get('database','DATABASE_PASSWORD'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#Admin
REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 2
REGISTRATION_AUTO_LOGIN = True
LOGIN_REDIRECT_URL = '/gen/dashboard/'
LOGIN_URL = '/accounts/login/'

#Templates

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS=(TEMPLATE_PATH,)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    STATIC_PATH,
)

#Flat Pages Settings
SITE_ID = 3
