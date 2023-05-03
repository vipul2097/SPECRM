#Creating the Base Image
FROM python:3.10-bullseye

#Setting Up Environment Variables in Docker Container
ENV DockerHOME=/app

#Setting Work Directory (In this your actual code resides)
RUN mkdir -p ${DockerHOME}

#Present Work Directory
WORKDIR ${DockerHOME}

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

# install dependencies  
RUN pip install --upgrade pip  

#Checking the network adapters inside the docker container
RUN apk add netcat-openbsd 

#Copy our whole project into our docker "app" directory
COPY ./SPE PROJECT ${DockerHOME}




