#This Docker file is a series of instructions which provide the layers to create a docker image (template) which runs as a container
#Creating base layer/ base image for image which is in this case is in python
#Creating working directory for subsequent commands
#Installing flask framework in the container so that the web app can run
#Specifying the port number that the container will listen on
#Shows which commands to run when the container starts

FROM  python:3.14-slim
WORKDIR  /app
COPY   . .
# deps needed to build mysqlclient
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir flask mysqlclient
EXPOSE 5002
CMD    ["python" , "app.py"]

# mysqlclient package is needed to connect to the MySQLdb  from within our python app
# custom network needed to connect the flask app to the mysql database container - (docker network create my-custom-network)
