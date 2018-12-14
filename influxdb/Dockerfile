FROM centos:7

RUN yum -y install epel-release && \
    yum -y update

RUN yum install -y sudo vim fping telnet openssh-server
ADD influxdb.repo /etc/yum.repos.d/influxdb.repo

RUN sudo yum -y install influxdb

ADD influxdb.conf /etc/influxdb/influxdb.conf

VOLUME /var/lib/influxdb
EXPOSE 8086
COPY entrypoint.sh /entrypoint.sh
COPY init-influxdb.sh /init-influxdb.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["influxd"]