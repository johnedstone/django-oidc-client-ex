### Purpose ###
- Demonstrates using OpenID Connect Client with python (django)
- Code works on traditional webserver as well as Origin/Openshift (PaaS) below.

### Notes django-oidc ###
- Prior to 18-Sep-2017: using python 3.4 and django 1.9 and a custom docker image
- 18-Sep-2017: using python:3.5 with no need for a custom docker image.
- Based on https://github.com/jhuapl-boss/django-oidc (python 3.x) which in turn is based on https://github.com/marcanpilami/django-oidc (python 2.x).  Behind the scenes, it uses Roland Hedberg's great pyoidc library.

### Notes on OIDC ###
- References:

    - [openid.net](http://openid.net/connect/)
    - [available libraries](http://openid.net/developers/libraries/)
    - [openid explained](https://connect2id.com/learn/openid-connect)

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


### To do: in order to get to django 1.10 ###
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

oc new-app --params django_oidc_client_params.txt -f openshift/templates/django-openshift.yaml


```
