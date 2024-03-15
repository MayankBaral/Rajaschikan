"""
Django settings for Rajaschikan project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sj0$7gw(!tz+jq#k#ew5m*1p4%l%^cirn@10s(h$jhcm1$a5lq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'homepage.apps.HomepageConfig',
    'user.apps.UserConfig',
    'django.contrib.auth',
    'crispy_forms',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "whitenoise.runserver_nostatic",
    'django.contrib.staticfiles',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Rajaschikan.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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

WSGI_APPLICATION = 'Rajaschikan.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Rajaschikan',
        'USER': 'rajaschikan',
        'PASSWORD': 'rajas2024',
        'HOST': 'rajaschikan.cnwawmkwku4x.ap-southeast-2.rds.amazonaws.com',
        'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

MEDIA_ROOT =  os.path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/'

STATIC_URL = 'https://rajaschikan.s3.amazonaws.com/static/'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#AUTH_USER_MODEL =
CSRF_TRUSTED_ORIGINS = ['https://9cb2-2401-4900-1c33-6ef6-ad79-45cb-fea8-b5b.ngrok-free.app']

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'home'

LOGIN_URL = 'login'

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')

AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT_ACL = None

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
    },
}



#STATIC_ROOT = os.path.join(BASE_DIR,'static')

#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR,'homepage/static')
#]


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

#DEFAULT_FILE_STORAGE = "storages.backends.s3.S3Storage"
#STATICFILES_STORAGE = "storages.backends.s3.S3Storage"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/