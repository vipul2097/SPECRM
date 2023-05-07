#Creating the Base Image
FROM python:3.10.7-alpine3.15

#Setting Up Environment Variables in Docker Container
ENV DockerHOME=/app

#Setting Work Directory (In this your actual code resides)
RUN mkdir -p $DockerHOME 

#Present Work Directory
WORKDIR $DockerHOME

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

# install dependencies  
RUN pip install --upgrade pip  

# install dependencies mysqlclient using mariadb connector and delete it after installation. 
RUN apk update && \
    apk add --no-cache mariadb-connector-c-dev && \
    apk add --no-cache python3 python3-dev mariadb-dev build-base && \
    pip3 install --no-cache-dir mysqlclient && \
    apk del python3-dev mariadb-dev build-base

# checking the network adapters inside the docker container
RUN apk add netcat-openbsd

# Copy the code contents to the /app directory.
COPY . $DockerHOME/

#Install the required dependencies.
RUN pip install -r requirements.txt

COPY wait.sh $DockerHOME/wait.sh
RUN chmod +x $DockerHOME/wait.sh

