"""
Django settings for Site project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xe7r&zuw1scx11qh)obx(d)v432k2n^#uzn2e=z8so$bdun0vs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0','localhost', '127.0.0.1','https://admissionsquare.in','admissionsquare.in','https://admassistant.fra1.digitaloceanspaces.com']


# Application definition

INSTALLED_APPS = [
    'tinymce',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'Site',
    
    'whitenoise.runserver_nostatic', 
    'storages',
    'Connect',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Site.urls'
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Site.context_processors.settings',
                'Site.context_processors.country_locations',
                'Site.context_processors.providers',
                'Site.context_processors.providers_courses',  
                'Site.context_processors.faqs',                
            ],
        },
    },
]

WSGI_APPLICATION = 'Site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    #}
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'AdmAssist',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
USE_SPACES = os.getenv('USE_SPACES') == 'TRUE'

if USE_SPACES:
    # settings
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_ENDPOINT_URL = 'https://fra1.digitaloceanspaces.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # static settings
    AWS_LOCATION = 'static'
    MEDIA_LOCATION = 'media'
    STATIC_URL = f'https://{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_ENDPOINT_URL}/{MEDIA_LOCATION}/'
    #STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' 
       
    STATICFILES_STORAGE = 'storage_backends.StaticStorage'
    DEFAULT_FILE_STORAGE = 'storage_backends.MediaStorage'   
else:   
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    #location where django collect all static files   
    STATIC_URL = '/static/' 
    STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles/")    
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR,"media/")

#location where you will store your static files
STATICFILES_DIRS = [os.path.join(BASE_DIR ,"static")]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#TINYMCE_JS_URL = "https://cdnjs.cloudflare.com/ajax/libs/tinymce/6.0.3/tinymce.min.js"#os.path.join(STATIC_URL, "tinymce/tinymce.min.js")
#TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "tinymce")
TINYMCE_DEFAULT_CONFIG = {

   'height': 360,

   'width': 1000,

   'cleanup_on_startup': True,

   'custom_undo_redo_levels': 20,

   'selector': 'textarea',

   'theme': 'silver',

   'plugins': '''

   textcolor save link image media preview codesample contextmenu

   table code lists fullscreen insertdatetime nonbreaking

   contextmenu directionality searchreplace wordcount visualblocks

   visualchars code fullscreen autolink lists charmap print hr

   anchor pagebreak

   ''',


   'toolbar1': '''

   fullscreen preview bold italic underline | fontselect,

   fontsizeselect | forecolor backcolor | alignleft alignright |

   aligncenter alignjustify | indent outdent | bullist numlist table |

   | link image media | codesample |

  

   ''',

   'toolbar2': '''

   visualblocks visualchars |

   charmap hr pagebreak nonbreaking anchor | code |

   ''',

   'contextmenu': 'formats | link image',

   'menubar': True,

   'statusbar': True,

   }
