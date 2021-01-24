# Dockerfile > docker build app > app image > docker run <image> > running app container
# To generate a Docker image we need to create a Dockerfile which contains instructions needed to
# build the image.
# The Dockerfile is then processed by the Docker builder which generates the Docker image.
# Then, with a simple 'docker run' command, we create and run a container with the Python service.

# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "python", "./server.py" ]