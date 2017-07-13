"""
Django settings for controller project.

Generated by 'django-admin startproject' using Django 1.9.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!tz^0(te#@tv5t1m_&b3k5)s$(xu+*x0m^7djwmf6-*=5lw_mj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'iot_platform.apps.IotPlatformConfig',
    'sensor.apps.SensorConfig'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'controller.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'controller/templates',
        ],
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

WSGI_APPLICATION = 'controller.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

#
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 10
}

# Kubernetes config
KUBE_API_DOMAIN = '128.199.242.5:8080'
CLOUD_KUBE_API_DOMAIN = '188.166.238.158:8080'
SENSOR_ORDINATOR_SERVICE_HOST = 'localhost:9090'
CONTENT_TYPE = {'JSON': "application/json", 'TEXT': 'text/plain'}
RESPONSE_JSON_TYPE_DEFINE = 'JSON'
RESPONSE_TEXT_TYPE_DEFINE = 'TEXT'

IOT_PLATFORM = {
    'onem2m': {
        'image': 'huanphan/onem2m:semi-final-4',
        'config': {'name': 'onem2m-config', 'mountPath': '/usr/src/ipe_config/config.cfg', 'subPath': 'config.cfg'},
        'item': {'name': 'onem2m-items', 'mountPath': '/usr/src/ipe_config/items.cfg', 'subPath': 'items.cfg'},
        'config_configmap': {'name': 'onem2m-config', 'key': 'config.cfg', 'path': 'config.cfg'},
        'item_configmap': {'name': 'onem2m-items', 'key': 'items.cfg', 'path': 'items.cfg'}
    },
    'openhab': {
        'image': 'huanphan/openhab:semi-final-6',
        'config': {'name': 'openhab-cfg', 'mountPath': '/openhab/configurations/openhab.cfg', 'subPath': 'openhab.cfg'},
        'item': {'name': 'openhab-items', 'mountPath': '/openhab/configurations/items/demo.items', 'subPath': 'demo.items'},
        'config_configmap': {'name': 'openhab-cfg', 'key': 'openhab.cfg', 'path': 'openhab.cfg'},
        'item_configmap': {'name': 'openhab-items', 'key': 'demo.items', 'path': 'demo.items'}
    }
}

SENSOR = {
        'image': 'huanphan/sensor-simulator:semi-final-qos',
        'config': {'name': 'sensor-config', 'mountPath': '/SimulateSensor/config/config.cfg', 'subPath': 'config.cfg'},
        'item': {'name': 'sensor-items', 'mountPath': '/SimulateSensor/config/items.cfg', 'subPath': 'items.cfg'},
        'config_configmap': {'name': 'sensor-config', 'key': 'config.cfg', 'path': 'config.cfg'},
        'item_configmap': {'name': 'sensor-items', 'key': 'items.cfg', 'path': 'items.cfg'}
}

