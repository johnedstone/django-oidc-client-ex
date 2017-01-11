#### Custom Docker images ####

For Origin/Openshift individual pip packages needed to be install as root

- cffi
- cryptography

#### Notes on docker build are below ####

```
# S2I
sudo docker build -t python34-libffi:latest .
sudo s2i build . python34-libffi:latest oidc:latest
sudo ./django_oidc_client_ex.localhost.docker.run.sh # this unsets/sets os vars
# sudo ./django_oidc_client_ex.prd.docker.run.sh

# Openshift
sudo docker build -t python34-libffi:latest . 
oc get svc -n default # get IP for internal docker registry
sudo docker tag 3af07aae3d66 <internal docker IP>:5000/openshift/python34-libffi:latest
oc whoami -t # get token
sudo docker login -u userid -p <token> <internal docker IP>:5000
sudo docker push <internal docker IP>:5000/openshift/python34-libffi:latest
oc get is -n openshift |egrep libffi # verify
```

#### Notes on querying origin ####

```
wget -q -S -O /dev/null --no-check-certificate --header='Host: django-oidc-client-hoo.apps.10.2.2.2.xip.io' 'http://192.168.2.14/myapp/public/'
  HTTP/1.1 200 OK
  Server: gunicorn/19.6.0
  Date: Wed, 11 Jan 2017 07:47:03 GMT
  Transfer-Encoding: chunked
  X-Frame-Options: SAMEORIGIN
  Vary: Cookie
  Content-Type: text/html; charset=utf-8
  Set-Cookie: 88d63a70d27974bc27bc78b1d7421a2c=4662b81cf4715a1daeb45dfcc38bb682; path=/; HttpOnly
  Cache-control: private
```
