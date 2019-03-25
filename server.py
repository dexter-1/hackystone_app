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

from hackystone_app import tag_position_calculator


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
r = redis.Redis(host=config_parser.get_redis_config('host'),
				port=config_parser.get_redis_config('port'),
				db=0)
TagPositionCalculator = tag_position_calculator.TagPositionCalculator(r)

tagId = "0"

@app.route("/")
def root():
	return app.send_static_file('index.html')

@app.route("/get_anchors")
def GetAnchors():
	return jsonify(anchors)

@app.route("/upload_tag_ping", methods=["POST"])
def HandleTagUpload():
	predictedPosition = TagPositionCalculator.compute_tag_position(r, tagId)
	if (predictedPosition != [None, None]).all():
		print("Predicted Position: [%f, %f]" %(predictedPosition[0], predictedPosition[1]))
	if request.method == "POST":
		data = request.json
		#pp = pprint.PrettyPrinter(indent=4)
		#pp.pprint(data)

		anchorId = data['anchorId']
		timestamp = time.time()
		averageRSSI = 0
		N = 0
		for ping in data['data']:
			averageRSSI += ping['rssi']
			N += 1
		if N != 0:
			averageRSSI = averageRSSI/float(N)
			m = measurement.Measurement(
				str(anchorId), str(ping['tagId']), str(averageRSSI), timestamp)
			m.save(r)

		return json.dumps(data)



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
