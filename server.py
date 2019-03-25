import time
import random
import threading
import json
import pprint
import redis

from flask import Flask
from flask import jsonify
from flask import request
from flask_socketio import SocketIO, send, emit

from models import measurement
from utils import config_parser


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app, message_queue="redis://")


@app.route("/")
def root():
	return app.send_static_file('index.html')

@app.route("/get_anchors")
def GetAnchors():
	return jsonify(anchors)

@app.route("/upload_tag_ping", methods=["POST"])
def HandleTagUpload():
	if request.method == "POST":
		data = request.json
		pp = pprint.PrettyPrinter(indent=4)
		pp.pprint(data)

		anchorId = data['anchorId']
		timestamp = time.time()

		for ping in data['data']:
			m = measurement.Measurement(
				anchorId, ping['tagId'], ping['rssi'], timestamp)
			r = redis.Redis(
				host=config_parser.get_redis_config('host'),
				port=config_parser.get_redis_config('port'),
				db=0
			)
			m.save(r)

		return json.dumps(data)

@socketio.on('connect')
def Connect():
	print('Connected to client socket')


if __name__ == "__main__":
	# Dispatch the Flask app on another thread to handle
	# HTTP requests in the background while computation and
	# data collection run on main thread
	thread = threading.Thread(
		target=socketio.run, args=(app,),
		kwargs={'use_reloader': False, 'host': '172.20.10.3', 'port': 5000}
	)
	thread.start()

'''
	socket = SocketIO(message_queue="redis://")

	# This is where data collection from beacons and
	# triangulation algorithms will go. For now,
	# the code below just sends random tag coordinates
	# through the socket to test the front end
	x = 50
	y = 50
	while x < 720:
		x += 1
		y += random.randint(-1, 1)
		tag = {'tagId': 0, 'x': x, 'y': y}
		socket.emit('tags', tag)
		time.sleep(0.100)
'''
