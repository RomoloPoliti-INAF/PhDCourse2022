FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-dev
COPY ./requirements.txt /root/requirements.txt
WORKDIR /root
RUN pip install -r requirements.txt
WORKDIR /flask
ENTRYPOINT [ "python3" ] 
CMD [ "myapp.py" ]
# EXPOSE 5010/tcp