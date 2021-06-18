"""
Django settings for movie_forest project.

Generated by 'django-admin startproject' using Django 3.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from django.contrib.messages import constants as messages
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-*65y(m&u)cp4v@pn1fuwiib2%2oo29_&*djtyzt*a(&+5)vgve"
# os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG  = True

ALLOWED_HOSTS = ["moviesforest.herokuapp.com" , "localhost" , "smacker-hacker-1-movies-forest.zeet.app" , "www.themoviesforest.gq", "themoviesforest.gq"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'home.apps.HomeConfig',
    'forest.apps.ForestConfig',
    'django.contrib.sites', #adding sites app for generating table to store my site domain 
    'django.contrib.sitemaps', #adding django sitemap framwork
    'webpush' #adding webpush application 

]
WEBPUSH_SETTINGS = {
    "VAPID_PUBLIC_KEY": "BJtONiMez_26DsFud8Ptpf57BHMkJmohEg61MhcmtibKMi3ltpwMTXN0SAnEaNpwg_Ol6roBTKh7-Yf-hPlRj6k",
    "VAPID_PRIVATE_KEY":"4A79z7VP6g1VZYbWkW3ric3YIQ_MiiTnw5QrLRsFZiM",
    "VAPID_ADMIN_EMAIL": "hp354998@gmail.com"
}

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'movie_forest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'movie_forest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# mannully added by JUFFLER
# asking a djang from where it needs to fetch static files
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static'),]
# giving a location to django for where it need to save fetched files
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# mannuly by himanshu
MESSAGE_TAGS = {
    messages.ERROR : "danger"
}



