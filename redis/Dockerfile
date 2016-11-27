FROM        ubuntu
#
MAINTAINER  <Author name and email address>
#       Update ubuntu and install redis-server
RUN         apt-get update && apt-get install -y redis-server
#       Expose redis-server port 6379
EXPOSE      6379
#       Run redis-server
ENTRYPOINT  ["/usr/bin/redis-server"]
