# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

#Install git-crypt
USER root
RUN apt-get update && apt-get install -y libssl-dev && apt-get install unzip
RUN cd /tmp && wget https://github.com/AGWA/git-crypt/archive/0.5.0.zip \
    && unzip 0.5.0.zip \
    && cd git-crypt-0.5.0/ \
    && make && make install

COPY --chown=777 /keys /tmp/keys
