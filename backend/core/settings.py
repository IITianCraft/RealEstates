# # # from pathlib import Path
# # # from decouple import config
# # # from datetime import timedelta
# # # import os

# # # BASE_DIR = Path(__file__).resolve().parent.parent

# # # SECRET_KEY = config('SECRET_KEY')

# # # DEBUG = config('DEBUG', default=False, cast=bool)

# # # ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# # # INSTALLED_APPS = [
# # #     'django.contrib.admin',
# # #     'django.contrib.auth',
# # #     'django.contrib.contenttypes',
# # #     'django.contrib.sessions',
# # #     'django.contrib.messages',
# # #     'django.contrib.staticfiles',
# # #     'rest_framework',
# # #     'rest_framework_simplejwt',
# # #     'rest_framework_simplejwt.token_blacklist',    
# # #     'corsheaders',
# # #     'users',
# # # ]

# # # REST_FRAMEWORK = {
# # #     'DEFAULT_AUTHENTICATION_CLASSES': (
# # #         'rest_framework_simplejwt.authentication.JWTAuthentication',
# # #     )
# # # }

# # # MIDDLEWARE = [
# # #     'django.middleware.security.SecurityMiddleware',
# # #     'django.contrib.sessions.middleware.SessionMiddleware',
# # #     'django.middleware.common.CommonMiddleware',
# # #     'django.middleware.csrf.CsrfViewMiddleware',
# # #     'django.contrib.auth.middleware.AuthenticationMiddleware',
# # #     'django.contrib.messages.middleware.MessageMiddleware',
# # #     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# # #     'corsheaders.middleware.CorsMiddleware',
# # # ]
# # # SIMPLE_JWT = {
# # #    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
# # #     "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
# # #     "ROTATE_REFRESH_TOKENS":  True,
# # #     "BLACKLIST_AFTER_ROTATION": True,
# # #     "AUTH_HEADER_TYPES": ("Bearer",),
# # #     "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
# # # }

# # # ROOT_URLCONF = 'core.urls'

# # # TEMPLATES = [
# # #     {
# # #         'BACKEND': 'django.template.backends.django.DjangoTemplates',
# # #         'DIRS': [os.path.join(BASE_DIR, 'templates')],    
# # #         'APP_DIRS': True,
# # #         'OPTIONS': {
# # #             'context_processors': [
# # #                 'django.template.context_processors.request',
# # #                 'django.contrib.auth.context_processors.auth',
# # #                 'django.contrib.messages.context_processors.messages',
# # #             ],
# # #         },
# # #     },
# # # ]

# # # WSGI_APPLICATION = 'core.wsgi.application'

# # # DATABASES = {
# # #     'default': {
# # #         'ENGINE': 'django.db.backends.postgresql',
# # #         'NAME': config('DB_NAME'),
# # #         'USER': config('DB_USER'),
# # #         'PASSWORD': config('DB_PASSWORD'),
# # #         'HOST': config('DB_HOST', default='localhost'),
# # #         'PORT': config('DB_PORT', default='5432'),
# # #     }
# # # }

# # # AUTH_PASSWORD_VALIDATORS = [
# # #     {
# # #         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
# # #     },
# # #     {
# # #         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
# # #     },
# # #     {
# # #         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
# # #     },
# # #     {
# # #         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
# # #     },
# # # ]

# # # LANGUAGE_CODE = 'en-us'

# # # TIME_ZONE = 'UTC'

# # # USE_I18N = True

# # # USE_TZ = True

# # # STATIC_URL = 'static/'

# # # DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# # # CORS_ALLOW_ALL_ORIGINS = True
# # # AUTH_USER_MODEL = 'users.CustomUser'

# # # MEDIA_URL = '/media/'
# # # MEDIA_ROOT = BASE_DIR / 'media'

# # # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# # # EMAIL_HOST = config('EMAIL_HOST')
# # # EMAIL_PORT = config('EMAIL_PORT', cast=int)
# # # EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
# # # EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# # # EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# # # DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
# # # SERVER_EMAIL = DEFAULT_FROM_EMAIL

# # # FRONTEND_URL = config('FRONTEND_URL')
# # # SITE_NAME = config('SITE_NAME')





# # from pathlib import Path
# # from decouple import config, Csv
# # from datetime import timedelta
# # import os

# # BASE_DIR = Path(__file__).resolve().parent.parent

# # SECRET_KEY = config('SECRET_KEY')

# # DEBUG = config('DEBUG', default=False, cast=bool)

# # ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())  # Use Csv() to split on commas

# # INSTALLED_APPS = [
# #     'django.contrib.admin',
# #     'django.contrib.auth',
# #     'django.contrib.contenttypes',
# #     'django.contrib.sessions',
# #     'django.contrib.messages',
# #     'django.contrib.staticfiles',
# #     'rest_framework',
# #     'rest_framework_simplejwt',
# #     'rest_framework_simplejwt.token_blacklist',
# #     'corsheaders',
# #     'users',
# # ]

# # REST_FRAMEWORK = {
# #     'DEFAULT_AUTHENTICATION_CLASSES': (
# #         'rest_framework_simplejwt.authentication.JWTAuthentication',
# #     ),
# # }

# # MIDDLEWARE = [
# #     'django.middleware.security.SecurityMiddleware',
# #     'corsheaders.middleware.CorsMiddleware',               # <- Place CorsMiddleware as high as possible
# #     'django.contrib.sessions.middleware.SessionMiddleware',
# #     'django.middleware.common.CommonMiddleware',
# #     'django.middleware.csrf.CsrfViewMiddleware',
# #     'django.contrib.auth.middleware.AuthenticationMiddleware',
# #     'django.contrib.messages.middleware.MessageMiddleware',
# #     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# # ]

# # SIMPLE_JWT = {
# #     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
# #     "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
# #     "ROTATE_REFRESH_TOKENS": True,
# #     "BLACKLIST_AFTER_ROTATION": True,
# #     "AUTH_HEADER_TYPES": ("Bearer",),
# #     "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
# # }

# # ROOT_URLCONF = 'core.urls'

# # TEMPLATES = [
# #     {
# #         'BACKEND': 'django.template.backends.django.DjangoTemplates',
# #         'DIRS': [os.path.join(BASE_DIR, 'templates')],
# #         'APP_DIRS': True,
# #         'OPTIONS': {
# #             'context_processors': [
# #                 'django.template.context_processors.request',
# #                 'django.contrib.auth.context_processors.auth',
# #                 'django.contrib.messages.context_processors.messages',
# #             ],
# #         },
# #     },
# # ]

# # WSGI_APPLICATION = 'core.wsgi.application'

# # # DATABASES using DATABASE_URL if set, otherwise fallback to individual configs
# # from dj_database_url import config as db_config

# # DATABASES = {
# #     'default': db_config(default=None) or {
# #         'ENGINE': 'django.db.backends.postgresql',
# #         'NAME': config('DB_NAME', default='postgres'),
# #         'USER': config('DB_USER', default='postgres'),
# #         'PASSWORD': config('DB_PASSWORD', default=''),
# #         'HOST': config('DB_HOST', default='localhost'),
# #         'PORT': config('DB_PORT', default='5432'),
# #     }
# # }

# # AUTH_PASSWORD_VALIDATORS = [
# #     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
# #     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
# #     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
# #     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
# # ]

# # LANGUAGE_CODE = 'en-us'

# # TIME_ZONE = 'UTC'

# # USE_I18N = True
# # USE_L10N = True
# # USE_TZ = True

# # STATIC_URL = '/static/'
# # STATIC_ROOT = BASE_DIR / 'staticfiles'

# # MEDIA_URL = '/media/'
# # MEDIA_ROOT = BASE_DIR / 'media'

# # DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # CORS_ALLOW_ALL_ORIGINS = True

# # AUTH_USER_MODEL = 'users.CustomUser'

# # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# # EMAIL_HOST = config('EMAIL_HOST')
# # EMAIL_PORT = config('EMAIL_PORT', cast=int)
# # EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
# # EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# # EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# # DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
# # SERVER_EMAIL = DEFAULT_FROM_EMAIL

# # FRONTEND_URL = config('FRONTEND_URL')
# # SITE_NAME = config('SITE_NAME')



# from pathlib import Path
# from decouple import config, Csv
# from datetime import timedelta
# import os

# BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = config('SECRET_KEY')
# DEBUG = config('DEBUG', default=False, cast=bool)
# ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework',
#     'rest_framework_simplejwt',
#     'rest_framework_simplejwt.token_blacklist',
#     'corsheaders',
#     'users',
# ]

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),
# }

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'corsheaders.middleware.CorsMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
#     "ROTATE_REFRESH_TOKENS": True,
#     "BLACKLIST_AFTER_ROTATION": True,
#     "AUTH_HEADER_TYPES": ("Bearer",),
#     "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
# }

# ROOT_URLCONF = 'core.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'core.wsgi.application'

# from dj_database_url import config as db_config

# DATABASES = {
#     'default': db_config(default=None) or {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME', default='homefinder_e4xw'),
#         'USER': config('DB_USER', default='homefinder_e4xw_user'),
#         'PASSWORD': config('DB_PASSWORD', default='TrkPAuSHfinsTZMvCfWxcCGUL1MoIWeG'),
#         'HOST': config('DB_HOST', default='dpg-d2erecsc94c739afu80-a'),
#         'PORT': config('DB_PORT', default='5432'),
#     }
# }

# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
# ]

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# CORS_ALLOW_ALL_ORIGINS = True
# AUTH_USER_MODEL = 'users.CustomUser'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_PORT = config('EMAIL_PORT', cast=int)
# EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
# SERVER_EMAIL = DEFAULT_FROM_EMAIL

# FRONTEND_URL = config('FRONTEND_URL')
# SITE_NAME = config('SITE_NAME')




# backend/core/settings.py    
from pathlib import Path
from decouple import config
from datetime import timedelta
import os
import dj_database_url

# -------------------------
# BASE DIR
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# SECURITY
# -------------------------
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

# The fix is here:
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# -------------------------
# APPS
# -------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',

    # Local apps
    'users',
]

# -------------------------
# REST FRAMEWORK / JWT
# -------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

# -------------------------
# MIDDLEWARE
# -------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Static files 
]

# -------------------------
# URLS / WSGI
# -------------------------
ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'

# -------------------------
# TEMPLATES (needed for admin)
# -------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add your custom templates folder if any
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

# -------------------------
# DATABASE
# -------------------------
if 'DATABASE_URL' in os.environ:
    # On Render, use the DATABASE_URL environment variable.
    # The `conn_max_age` is a good practice for pooled connections.
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
            conn_health_checks=True,
            ssl_require=True
        )
    }
else:
    # Fallback to local settings from a .env file.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME', default='mydatabase'),
            'USER': config('DB_USER', default='myuser'),
            'PASSWORD': config('DB_PASSWORD', default='mypassword'),
            'HOST': config('DB_HOST', default='localhost'),
            'PORT': config('DB_PORT', default='5432'),
        }
    }

# -------------------------
# PASSWORD VALIDATION
# -------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------
# LANGUAGE / TIME
# -------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------------
# STATIC & MEDIA FILES
# -------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -------------------------
# CUSTOM USER
# -------------------------
AUTH_USER_MODEL = 'users.CustomUser'

# -------------------------
# CORS
# -------------------------
CORS_ALLOW_ALL_ORIGINS = True

# -------------------------
# EMAIL SETTINGS
# -------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# -------------------------
# SITE INFO
# -------------------------
FRONTEND_URL = config('FRONTEND_URL')
SITE_NAME = config('SITE_NAME')

# -------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# -------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'