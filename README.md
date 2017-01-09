### Notes ###
- Currently using python 3.4 and django 1.9
- Based on https://github.com/jhuapl-boss/django-oidc (python 3.x) which in turn is based on https://github.com/marcanpilami/django-oidc (python 2.x).  Behind the scenes, it uses Roland Hedberg's great pyoidc library.

### Purpose ###
- Demonstrates using OpenID Connect Client with django
- This code base works both on a tradition webserver as well as Origin/Openshift PaaS

### To do in order to get to django 1.10 ###
- django-braces has a url problem - maybe the same as djangooidc, below
- and djangooidc has a warning that needs to be resolved, for django 1.10: django.conf.urls.patterns() is deprecated 

### Origin/Openshift ###
Notes for Openshift:

- Based on Openshift Django Example [link](https://github.com/openshift/django-ex)
- Copied wsgi.py up one level to be compatible with Origin/Openshift
- Example creating a new app:

```
oc new-app -f openshift/templates/django.yaml --params="\
SOURCE_REPOSITORY_URL=${SOURCE_REPOSITORY_URL},\
CONTEXT_DIR=${CONTEXT_DIR},\
APPLICATION_DOMAIN=${APPLICATION_DOMAIN},\
PIP_PROXY=${PIP_PROXY},\
DEBUG=${DEBUG},\
SECRET_KEY=${SECRET_KEY},\
ADMIN_URL=${ADMIN_URL},\
OP_NAME=${OP_NAME},\
SCOPE=${SCOPE},\
AUTHORIZATION_ENDPOINT=${AUTHORIZATION_ENDPOINT},\
TOKEN_ENDPOINT=${TOKEN_ENDPOINT},\
USERINFO_ENDPOINT=${USERINFO_ENDPOINT},\
ISSUER=${ISSUER},\
JWKS_URI=${JWKS_URI},\
CLIENT_ID=${CLIENT_ID},\
CLIENT_SECRET=${CLIENT_SECRET},\
REDIRECT_URIS=${REDIRECT_URIS},\
POST_LOGOUT_REDIRECT_URIS=${POST_LOGOUT_REDIRECT_URIS}"
```
