FROM centos
COPY ./python_http_req.py /root/send_req.py
RUN chmod +x /root/send_req.py
ENTRYPOINT /root/send_req.py
