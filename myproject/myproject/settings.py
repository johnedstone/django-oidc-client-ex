import os
from unipath import Path

BASE_DIR = Path(__file__).ancestor(2)

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

ADMIN_URL = os.environ.get('ADMIN_URL', 'admin')

INTERNAL_IPS = ['127.0.0.1',]

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR.child('collect_static') 

SITE_ID = 1

# Start: Used to go directly to the OP 
# LOGIN_URL='myproject_login'
OP_NAME = os.environ.get('OP_NAME')
# Some day figure out how to do this with URL Namespace
LOGIN_URL = '/openid/openid/{}'.format(OP_NAME)
# LOGIN_REDIRECT_URL = 'myapp:private'
# End: Used to go directly to the OP 

# djangooidc
AUTHENTICATION_BACKENDS = [
'django.contrib.auth.backends.ModelBackend',
'djangooidc.backends.OpenIdConnectBackend',
]

OP_NAME = os.environ.get('OP_NAME')

BEHAVIOR = {
    "response_type": "code",
    "scope": os.environ.get('SCOPE').split(',')
}

PROVIDER_INFO = {
    'authorization_endpoint': os.environ.get('AUTHORIZATION_ENDPOINT'),
    'token_endpoint': os.environ.get('TOKEN_ENDPOINT'), 
    'userinfo_endpoint': os.environ.get('USERINFO_ENDPOINT'), 
    'issuer': os.environ.get('ISSUER'), 
    'jwks_uri': os.environ.get('JWKS_URI'), 
}

OIDC_PROVIDERS = {
    OP_NAME: {
        'behaviour': BEHAVIOR,
        'client_registration': {
            'client_id': os.environ.get('CLIENT_ID'),
            'client_secret': os.environ.get('CLIENT_SECRET'),
            'redirect_uris': os.environ.get('REDIRECT_URIS').split(','),
            'post_logout_redirect_uris': os.environ.get('POST_LOGOUT_REDIRECT_URIS').split(','),
        },
        'provider_info': PROVIDER_INFO,
    },
}
