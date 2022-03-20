FROM ubuntu

#Set up Ubuntu
RUN bash
RUN apt-get update && \
    apt-get install -y lsb-release && \
    apt-get clean all && \
    apt-get install -y build-essential libssl-dev libffi-dev python-dev && \
    apt-get install -y git && \
    mkdir /home/kevin

#Set up Python
RUN apt-get install -y python3-pip && \
    apt-get install -y python3-venv



#Add dev files
COPY DEV /tmp
COPY tmp /tmp




