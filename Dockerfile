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
# RUN pip install --no-cache-dir -r requirements.txt
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#         build-essential \
#         default-libmysqlclient-dev \
#         && rm -rf /var/lib/apt/lists/*
RUN apk update && \
    apk add --no-cache mariadb-connector-c-dev && \
    apk add --no-cache python3 python3-dev mariadb-dev build-base && \
    pip3 install --no-cache-dir mysqlclient && \
    apk del python3-dev mariadb-dev build-base

# Checking the network adapters inside the docker container
RUN apk add netcat-openbsd 

#Copy our whole project into our docker "app" directory in the container.
COPY . $DockerHOME

# Install the required depedencies.
RUN pip install --no-cache-dir -r requirements.txt

# We will now run the wait.sh file with the required permissions.
RUN chmod +x wait.sh


