# FROM centos/python-34-centos7 # for origin s2i
# FROM openshift3/python-33-rhel7 # to work around rhscl - not needed

# for openshift
FROM rhscl/python-34-rhel7:latest
MAINTAINER johnedstone <johnedstone@gmail.com>
USER root
RUN  yum --nogpgcheck install -y \
    libffi libffi-devel openssl openssl-devel openssl-libs \
    &&  yum --enablerepo=\* clean all
USER 1001
