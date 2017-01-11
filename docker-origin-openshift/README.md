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
