FROM ubuntu:16.04 
MAINTAINER JD TOTOW <totow@unipi.gr>
RUN apt-get update
RUN apt-get install -y python3 python3-pip 
RUN pip3 install flask pymongo 
RUN mkdir /app
RUN mkdir -p /app/data
COPY service.py /app/service.py  
ADD data /app/data 
WORKDIR /app
ENTRYPOINT [ "python3","-u", "service.py" ]
