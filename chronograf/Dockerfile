FROM centos:7

RUN yum -y install epel-release && \
    yum -y update

RUN yum install -y sudo vim fping telnet wget openssh-server

RUN wget https://dl.influxdata.com/chronograf/releases/chronograf-1.7.4.x86_64.rpm
RUN sudo yum -y localinstall chronograf-1.7.4.x86_64.rpm
ADD ./influx_db.src /usr/share/chronograf/resources/influx_db.src
EXPOSE 8888

CMD ["/usr/bin/chronograf", "-b", "/var/lib/chronograf/chronograf-v1.db", "-c", "/usr/share/chronograf/canned"]