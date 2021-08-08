FROM centos:7
RUN yum install -y vim
RUN yum install -y python36
RUN yum install -y nfs-utils
RUN pip3 install requests
RUN mkdir -p /pyhttp/
COPY files/*.py /pyhttp/
RUN chmod +x /pyhttp/*.py
EXPOSE 7000
CMD /usr/bin/python3 /pyhttp/writeIndex.py
