from pathlib import Path
import os
from dotenv import load_dotenv 
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("secret_key")
DEBUG = True
ALLOWED_HOSTS = [".vercel.app","127.0.0.1"]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Main',
    'crispy_forms',
    "crispy_bootstrap4",
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'CopyPaste.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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
WSGI_APPLICATION = 'CopyPaste.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER':'postgres',
        'PASSWORD': os.environ.get('dbpass'),
        'HOST': 'viaduct.proxy.rlwy.net',
        'PORT': '24653'
    }
}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = 'static/'
MEDIA_URL = 'tmp/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'tmp/media')


