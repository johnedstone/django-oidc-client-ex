#### Adding missing libffi rpm ####

```
# S2I
sudo docker build -t python34-libffi:latest . # currently errors on libffi-devel on post-install

./s2i build . python34-libffi:latest oidc # as user - currently errors on files missing and couldn't run collectstatic

sudo ./django_oidc_client_ex.localhost.docker.run.sh

# Openshift
sudo docker build -t python34-libffi:latest . # currently errors on libffi-devel on post-install

oc get svc -n default # get IP for internal docker registry

sudo docker tag 3af07aae3d66 <internal docker IP>:5000/openshift/python34-libffi:latest

oc whoami -t # get token

sudo docker login -u userid -p <token> <internal docker IP>:5000

sudo docker push <internal docker IP>:5000/openshift/python34-libffi:latest

oc get is -n openshift |egrep libffi # verify


# do origin new-project/new-app
# delete local pip files
```
