"""
Django settings for settings project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent #полный путь от корня до дериктории (то есть с папки проекта)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7av%6spa7s%mpk9m9sb=+(00sf=0aitz=1za*&&1rwslhgk8o#' #ключ для шифрования

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #для контроля вывода ошибок

ALLOWED_HOSTS = [] #сервера, откуда могут призодить запросы
# Application definition

INSTALLED_APPS = [                      #список с приложениями, зарезерв в проекте (указывается класс из apps)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'colorfield',
    'ckeditor',


    'bboard.apps.BboardConfig'
]

MIDDLEWARE = [                                          # как и installed_apps, но только действует на всех, грубо говоря ПО для сервака
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'settings.urls'   #просто ссылка на стартовый url

TEMPLATES = [                                           #Настройки для шаблонизатора
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'] #указывает папку со всякими статическими файлами (html и всякая пурга), пример, где используется BaseDir
        ,
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

WSGI_APPLICATION = 'settings.wsgi.application'  #отвечает за синхронность/асинхронность (если нужен асинхронный, то исп ASGI)


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {                                   # насторойка БД
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',   #указание нашей бд (разбрать, как ставить удаленные бд)
        'NAME': BASE_DIR / 'db.sqlite3',     # как называть БД, если ее не существует
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [                #валидатор для пароля
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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us' #язык, на котором изначальная Апишка (начальный сайт)

TIME_ZONE = 'UTC' #временная зона

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/' #путь для всяких статических штук

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' #тип данных, который использутся в приложениях по умолчанию (id такого типа), всегда подставляется в новое созданное приложение в apps
