FROM        python:2.7
#
MAINTAINER  <Author name and email address>
#       Update python image
RUN         apt-get update -y
#
ADD         . /code
WORKDIR     /code
#       upgrade pip
RUN         pip install --upgrade pip
#
RUN         pip install -r requirements.txt
#
CMD         python app.py
