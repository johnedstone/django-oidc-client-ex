### Notes ###
- Currently using python 3.4 and django 1.9
- Based on https://github.com/jhuapl-boss/django-oidc (python 3.x) which in turn is based on https://github.com/marcanpilami/django-oidc (python 2.x).  Behind the scenes, it uses Roland Hedberg's great pyoidc library.

### Purpose ###
- Demonstrates using OpenID Connect Client with django
- Code works on tradition webserver as well as Origin/Openshift (PaaS) below.

### Notes on OIDC ###
- References: [link](http://openid.net/connect/)
- What do you need to provide to the OpenID Provider (OP)?
    - Redirection URI(s) 
    - Scope, e.g. openid profile email auth_web
- The OP will then provide you with the following:
    - Client ID
    - Client Secret
    - Authorization Endpoint
    - Token Endpoint
    - Userinfo Endpoint
    - Issuer
    - JWKS URI


### To do in order to get to django 1.10 ###
- django-braces has a url problem - maybe the same as djangooidc, below
- and djangooidc has a warning that needs to be resolved, for django 1.10: django.conf.urls.patterns() is deprecated 

### Origin/Openshift Notes ###

- Custom image was needed, see *docker-origin-openshift* folder 
- This project has extended the Openshift Django Example [link](https://github.com/openshift/django-ex) to demonstrate OIDC authentication
- Copied wsgi.py up one level to be compatible with Origin/Openshift

```
# Creating a new project in Origin/Openshift
oc secrets new-sshauth sshsecret --ssh-privatekey=$HOME/<path to key>
oc secret add serviceaccount/builder secrets/sshsecret

oc new-app -f openshift/templates/django.yaml --param="\
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
POST_LOGOUT_REDIRECT_URIS=${POST_LOGOUT_REDIRECT_URIS},\
GIT_PROJECT_URL=${GIT_PROJECT_URL}"
```
