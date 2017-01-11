import os
import hashlib
from unipath import Path

BASE_DIR = Path(__file__).ancestor(2)
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
     hashlib.sha1(os.urandom(128)).hexdigest(), 
)
DEBUG = os.environ.get('DEBUG', 'on') == 'on'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost 127.0.0.1').split()
ADMIN_URL = os.environ.get('ADMIN_URL', 'admin')
INTERNAL_IPS = os.environ.get('INTERNAL_IPS', 'localhost 127.0.0.1').split() 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'debug_toolbar',
    'myapp',
    'djangooidc',
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
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

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
                'myapp.context_processors.external_urls',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR.child('collect_static') 

SITE_ID = 1

# 30 min
SESSION_COOKIE_AGE = 60 * 30

OP_NAME = os.environ.get('OP_NAME', 'unknown_op_name')
LOGIN_URL = '/openid/openid/{}'.format(OP_NAME)

# djangooidc
AUTHENTICATION_BACKENDS = [
'django.contrib.auth.backends.ModelBackend',
'djangooidc.backends.OpenIdConnectBackend',
]


BEHAVIOR = {
    "response_type": "code",
    "scope": os.environ.get('SCOPE', 'unknown scope').split() # origin/openshift can't handle comma
}

PROVIDER_INFO = {
    'authorization_endpoint': os.environ.get('AUTHORIZATION_ENDPOINT', 'unknown_auth_endpoint'),
    'token_endpoint': os.environ.get('TOKEN_ENDPOINT', 'unknown_token_endpoint'), 
    'userinfo_endpoint': os.environ.get('USERINFO_ENDPOINT', 'unknown_userinfo_endpoint'), 
    'issuer': os.environ.get('ISSUER', 'unknown_issuer'), 
    'jwks_uri': os.environ.get('JWKS_URI', 'unknown_jwks_uri'), 
}

OIDC_PROVIDERS = {
    OP_NAME: {
        'behaviour': BEHAVIOR,
        'client_registration': {
            'client_id': os.environ.get('CLIENT_ID', 'unknown_id'),
            'client_secret': os.environ.get('CLIENT_SECRET', 'unknown_secret'),
            'redirect_uris': os.environ.get('REDIRECT_URIS', 'unknown_uris').split(),
            'post_logout_redirect_uris': os.environ.get('POST_LOGOUT_REDIRECT_URIS', 'unknown_post_uris').split(),
        },
        'provider_info': PROVIDER_INFO,
    },
}

ENABLE_SSL = os.environ.get('ENABLE_SSL', 'on') == 'on' # Added for origin/openshift
if not DEBUG and ENABLE_SSL:
   SECURE_SSL_REDIRECT = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
GIT_PROJECT_URL = os.environ.get('GIT_PROJECT_URL', '#')

# vim: ai et ts=4 sw=4 sts=4
