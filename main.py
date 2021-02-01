import flask
from gevent.pywsgi import WSGIServer
from threading import Thread
from flask import request, jsonify, render_template
import random
import os
import string
app = flask.Flask(__name__)

imagecount = len(os.listdir('images'))

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', imagecount=imagecount)


@app.route('/all', methods=['GET'])
def api_all():
    returned = {}
    print(os.listdir('images'))
    for i in os.listdir('images'):
      link = 'https://reaction.lol/images/' + i
      image = {i[8:26]: link}
      returned.update(image)
    return jsonify(returned)

@app.route('/get-<args>', methods=['GET'])
def api_custom(args):
  returned = {}
  for i in os.listdir('images'):
    if i == f'rlimage_{args}.png':
      returned = {
"url":f"https://reaction.lol/images/rlimage_{args}.png"
      }
  if returned == {}:
    returned = {"404"}
    return jsonify(returned)
  return jsonify(returned)



letters = string.ascii_letters


for i in os.listdir('images'):
  if not i[0:8] == 'rlimage_':
    id = ''.join(random.choice(letters) for i in range(18))
    id = 'rlimage_' + id
    os.rename('images/' + i, 'images/' + id + '.png')

@app.route('/image', methods=['GET'])
def api_filter():
    link = 'https://reaction.lol/images/' + random.choice(os.listdir('images'))
    image = {"url": link}
    return jsonify(image)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('home.html', imagecount=imagecount), 404

def run():
    http_server = WSGIServer(('0.0.0.0', 8080), app)
    http_server.serve_forever()


def keep_alive():
    server = Thread(target=run)
    server.start()

server = Thread(target=run)
server.start()

keep_alive()
