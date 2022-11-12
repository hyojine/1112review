from pathlib import Path
from environ import Env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
env = Env() 
env_path = BASE_DIR / ".env" 
if env_path.exists():
	with env_path.open("rt", encoding="utf8") as f:
		env.read_env(f, overwrite=True)

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
DATABASES = {
    'default': env.db(),

    'extra': env.db_url(
        'SQLITE_URL',
        default='sqlite:////tmp/my-tmp-sqlite.db'
    )
}

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'users',
]
REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
       
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
   
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_review.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'test_review.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

#### 위로 이동시켰지만 혹시 몰라서 둘다 남겨둠 ####
#### 도텐브 설정 from google ####
# from environ import Env

# env = Env() 
# env_path = BASE_DIR / ".env" 
# if env_path.exists():
# 	with env_path.open("rt", encoding="utf8") as f:
# 		env.read_env(f, overwrite=True)

# SECRET_KEY = env('SECRET_KEY')
# DEBUG = env('DEBUG')
# DATABASES = {
#     'default': env.db(),

#     'extra': env.db_url(
#         'SQLITE_URL',
#         default='sqlite:////tmp/my-tmp-sqlite.db'
#     )
# }

#### 도텐브 설정 from 공식문서 ####
# import environ
# import os

# env = environ.Env(
#     # set casting, default value
#     DEBUG=(bool, False)
# )

# # Set the project base directory
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Take environment variables from .env file
# environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# DEBUG = env('DEBUG')
# SECRET_KEY = env('SECRET_KEY')
# DATABASES = {
#     'default': env.db(),

#     'extra': env.db_url(
#         'SQLITE_URL',
#         default='sqlite:////tmp/my-tmp-sqlite.db'
#     )
# }