"""
Django settings for backend project.

Production-ready settings for:
- Render
- External MySQL
"""

# --------------------------------------------------
# IMPORTS
# --------------------------------------------------
from pathlib import Path
import os
import pymysql

# --------------------------------------------------
# PyMySQL CONFIG (Required)
# --------------------------------------------------

import pymysql
pymysql.install_as_MySQLdb()

# --------------------------------------------------
# BASE DIRECTORY
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------
# SECURITY SETTINGS
# --------------------------------------------------
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-local-only-key"
)

DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".onrender.com",
]

# --------------------------------------------------
# APPLICATION DEFINITION
# --------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party
    "rest_framework",

    # Local apps
    "app",
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

# --------------------------------------------------
# DJANGO REST FRAMEWORK (JWT)
# --------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

# --------------------------------------------------
# URLS & TEMPLATES
# --------------------------------------------------
ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

# --------------------------------------------------
# DATABASE CONFIG (External MySQL)
# --------------------------------------------------
from decouple import config

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", cast=bool)

from urllib.parse import urlparse
from decouple import config

db_url = urlparse(config("MYSQL_PUBLIC_URL"))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": db_url.path.lstrip("/"),
        "USER": db_url.username,
        "PASSWORD": db_url.password,
        "HOST": db_url.hostname,
        "PORT": db_url.port,
        "OPTIONS": {"charset": "utf8mb4"},
    }
}

# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------
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

# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --------------------------------------------------
# STATIC FILES (Render requirement)
# --------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# --------------------------------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# --------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
