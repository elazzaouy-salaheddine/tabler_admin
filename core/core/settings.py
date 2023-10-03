"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-c58d_(s8ceca)59(!n-d44rd@ai_kwctw$ykqs0%ta(_y6=u4c"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "ckeditor",
    'admin_volt.apps.AdminVoltConfig',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "apps.dashboard",
    "apps.crm",
    "apps.contact",
    "apps.emails",
    "apps.hospital",
    "apps.hr",
    "apps.school",
    "apps.task",
    # TODO create app base chatGPT3 API
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
# Add these new lines
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_ROOT = BASE_DIR / "uploads"

MEDIA_URL = "/uploads/"
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Email configurations
""" EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.xyz.com' # Set your emails host
EMAIL_PORT=587
EMAIL_HOST_USER='abc@xyz.com'
EMAIL_HOST_PASSWORD='******' #Your password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL = 'abc@xyz.com' """

LOGIN_URL = 'profiles:login_account'
LOGIN_REDIRECT_URL = 'dashboard_home'
LOGOUT_REDIRECT_URL = 'dashboard_home'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


CKEDITOR_UPLOAD_PATH = 'uploads/'  # This is the default upload path
CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',

        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
        ],

    },
}
