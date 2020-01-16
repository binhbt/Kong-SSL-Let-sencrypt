from flask import Flask, Response
import uuid
import os

app = Flask(__name__)
randomid = uuid.uuid4()
@app.route('/')
def index():
    hostname = os.uname()[1]
    from time import sleep
    sleep(0.5)
    return 'Container Hostname: ' + hostname + ' , ' + 'UUID: ' + str(randomid) + '\n'

@app.route('/public')
def hello_public():
  return 'User Hello from public!'

@app.route('/.well-known/acme-challenge/<challenge>')
def letsencrypt_check(challenge):
    challenge_response = {
        "<challenge_token>":"<challenge_response>",
        "<challenge_token>":"<challenge_response>"
    }
    return Response(challenge_response[challenge], mimetype='text/plain')

@app.route('/user/homepage')
def hello_homepage():
  return 'User Hello from homepage! You need logged in to access this page'
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)