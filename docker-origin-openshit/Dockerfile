FROM centos/python-34-centos7
# FROM rhscl/python-34-rhel7:latest
MAINTAINER johnedstone <johnedstone@gmail.com>
USER root
RUN  yum --nogpgcheck install -y \
    libffi \
    &&  yum --enablerepo=\* clean all
USER 1001
