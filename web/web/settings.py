"""
Django settings for web project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
#-
from django.utils.translation import gettext_lazy as _
#-
from misc import configuration
from misc.django_configuration import django_conf_adapter

# Setup config
_config = {} # pylint:disable=invalid-name
configuration.load_files_from_shell(_config, adapter=django_conf_adapter)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
ROOT_DIR = Path(os.environ['ROOT_DIR'])
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = _config['application.secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = _config.get('application.debug', False)

ALLOWED_HOSTS = _config.get('server.allowed_hosts', [])


# Application definition

INSTALLED_APPS = [
    'mail_domain',
    'mail_user',
    'mail_alias',
    'my_user',
    'website',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'carbondesign',
    'mailer',
    'rules',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
]

ROOT_URLCONF = 'web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.' + _config.get('database.engine',
            'sqlite3'),
        'NAME': _config.get('database.name', BASE_DIR/'db.sqlite3'),
        'HOST': _config.get('database.host'),
        'USER': _config.get('database.username'),
        'PASSWORD': _config.get('database.password'),
        'OPTIONS': _config.get('database.options', {}),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': _config.get('logging.handlers', {}),
    'root': {
        'handlers': ['console'],
        'level': _config.get('logging.level', 'INFO'),
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'my_user.User'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # pylint:disable=line-too-long
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # pylint:disable=line-too-long
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # pylint:disable=line-too-long
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # pylint:disable=line-too-long
    },
]

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = [
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

USE_I18N = True
LANGUAGE_CODE = 'id'
LANGUAGES = (
    ('id', _("Bahasa Indonesia")),
    ('en', _("English")),
)
LOCALE_PATHS = (
    BASE_DIR/'web'/'locale',
    BASE_DIR/'locale',
)

USE_L10N = True
USE_TZ = True
TIME_ZONE = 'Asia/Jakarta'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/assets/'
STATIC_ROOT = ROOT_DIR/_config.get('server.public_root', 'public/web')/'assets'
MEDIA_URL = '/uploads/'
MEDIA_ROOT = ROOT_DIR/'var'/'web'/'uploads'
STATICFILES_DIRS = [
    BASE_DIR/'static',
]
SVG_DIRS = [
    ROOT_DIR/'web'/'static_svg',
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SMTP

EMAIL_BACKEND = _config.get('smtp.backend',
        'django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = _config.get('smtp.host')
EMAIL_PORT = _config.get('smtp.port')
EMAIL_HOST_USER = _config.get('smtp.username')
EMAIL_HOST_PASSWORD = _config.get('smtp.password')
EMAIL_USE_TLS = _config.get('smtp.use_tls')
EMAIL_USE_SSL = _config.get('smtp.use_ssl')
DEFAULT_FROM_EMAIL = _config.get('application.email_from', EMAIL_HOST_USER)


## AllAuth

ACCOUNT_AUTHENTICATION_METHOD = _config.get('account.authentication_method',
        'username')
ACCOUNT_CONFIRM_EMAIL_ON_GET = _config.get('account.confirm_email_on_get',
        False)
ACCOUNT_EMAIL_REQUIRED = _config.get('account.email_required', False)
ACCOUNT_EMAIL_VERIFICATION = _config.get('account.email_verification',
        'optional')
ACCOUNT_LOGOUT_ON_GET = _config.get('account.logout_on_get', False)
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = _config.get(
        'account.logout_on_password_change', False)

#SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
}


_config = None # pylint:disable=invalid-name
