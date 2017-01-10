# FROM centos/python-34-centos7 # for origin s2i
# FROM rhscl/python-34-rhel7:latest # for openshift


# to work around rhscl
FROM openshift3/python-33-rhel7
MAINTAINER johnedstone <johnedstone@gmail.com>
USER root
RUN  yum --nogpgcheck install -y \
    libffi libffi-devel \
    &&  yum --enablerepo=\* clean all
USER 1001
