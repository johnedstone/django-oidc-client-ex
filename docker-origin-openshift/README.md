#### Adding missing libffi rpm ####

```
sudo docker build -t python34-libffi:latest . # currently errors on libffi-devel on post-install

./s2i build . python34-libffi:latest oidc # as user - currently errors on files missing and couldn't run collectstatic

sudo ./django_oidc_client_ex.localhost.docker.run.sh

# verify above docker run
# push image
# do origin new-project/new-app
# delete local pip files
```
