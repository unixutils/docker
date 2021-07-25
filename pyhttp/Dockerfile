FROM centos:latest
RUN yum install -y vim
RUN yum install -y python36
RUN mkdir -p /pyhttp/
COPY files/writeIndex.py /pyhttp/writeIndex.py
RUN chmod +x /pyhttp/writeIndex.py
EXPOSE 7000
CMD /usr/bin/python3 /pyhttp/writeIndex.py
