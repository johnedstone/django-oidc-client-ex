### Notes ###
- Currently using python 3.4 and django 1.9
- Based on https://github.com/jhuapl-boss/django-oidc (python 3.x) which in turn is based on https://github.com/marcanpilami/django-oidc (python 2.x).  Behind the scenes, it uses Roland Hedberg's great pyoidc library.

### Purpose ###
- Demonstrates using OpenID Connect Client with django

### To do in order to get to django 1.10 ###
- django-braces has a url problem - maybe the same as djangooidc, below
- and djangooidc has a warning that needs to be resolved, for django 1.10: django.conf.urls.patterns() is deprecated 

### Next step ###
- Develop this example for PaaS, e.g. OpenShift
