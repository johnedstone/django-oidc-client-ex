FROM centos/python-34-centos7:latest

# for openshift
# FROM rhscl/python-34-rhel7:latest
MAINTAINER johnedstone <johnedstone@gmail.com>
USER root
RUN  yum --nogpgcheck install -y \
    libffi-devel openssl-devel \
    &&  yum --enablerepo=\* clean all
RUN export LD_LIBRARY_PATH=/opt/rh/rh-python34/root/usr/lib64 \
  && /opt/rh/rh-python34/root/usr/bin/pip install cffi \
  && /opt/rh/rh-python34/root/usr/bin/pip install cryptography
#  && /opt/rh/rh-python34/root/usr/bin/pip --proxy <proxy ip:port> install cffi \
#  && /opt/rh/rh-python34/root/usr/bin/pip --proxy <proxy ip:port> install cryptography
USER 1001
