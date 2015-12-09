# ABFT checker container
FROM ubuntu
MAINTAINER Daniel Borlay <borlay.daniel@gmail.com> \
           Marton Toth <tothmarton33@gmail.com>

# Install dependencies
RUN apt-get -y update                       && \
    apt-get -y install python python-pip    && \
    pip install Flask

# Make Service environment
RUN mkdir -p /matrix/abft

# Add service files
ADD *.py /matrix/abft/

# Make server.py as entry point
ENTRYPOINT /matrix/abft/server.py

EXPOSE 8080
