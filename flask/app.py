from flask import Flask
from redis import Redis
import socket

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def webpagecounter():
    redis.incr('pagecount')
    return 'Docker Compose:  Page has been displayed %s times.  Contianer ID currently displaying page %s at IP address %s.'  % (redis.get('pagecount'), socket.gethostname(), socket.gethostbyname(socket.gethostname()))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
