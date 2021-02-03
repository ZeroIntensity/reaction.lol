import flask
from gevent.pywsgi import WSGIServer
from threading import Thread
from flask import request, jsonify, render_template
import random
import os
import string
from reaction_lol import getimage
app = flask.Flask(__name__)
from datetime import datetime
imagecount = len(os.listdir('images'))

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', imagecount=imagecount)

def readrequests():
  for i in os.listdir('requests'):
    f = open('requests/' + i)
    lines = f.readlines()
    print(lines[0])
    f.close()
    os.remove('requests/' + i)

readrequests()


@app.route('/all', methods=['GET'])
def api_all():
    returned = {}
    print(os.listdir('images'))
    for i in os.listdir('images'):
      link = 'https://reaction.lol/images/' + i
      image = {i[8:26]: link}
      returned.update(image)
    return jsonify(returned)

@app.route('/get?<args>', methods=['GET'])
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

@app.route('/tryit')
def tryit():
  return render_template('tryit.html', img=getimage())

@app.route('/submiturl', methods=['GET','POST'])
def submiturl():
  if request.method == 'POST':
    form_data = request.form.to_dict().get('imgurl')
    if not '.' in form_data:
      return render_template('submitfailed.html')
    now = datetime.now()
    f = open(now.strftime('requests/%b-%d-%Y_%H-%M-%S.txt'), 'w+')
    f.write(f'{form_data}')
    f.close()
    return render_template('submitsuccess.html')


@app.route('/submit')
def submit():
  return render_template('submit.html')


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


server = Thread(target=run)
server.start()

