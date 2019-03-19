from flask import Flask
from flask import jsonify
from flask_socketio import SocketIO, send, emit
import time
import random
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, message_queue="redis://")

# Sample anchor data
anchors = [
	{
		'anchorId': 0,
		'x': 240,
		'y': 100,
	},
	{
		'anchorId': 1,
		'x': 240,
		'y': 200,
	},
	{
		'anchorId': 2,
		'x': 240,
		'y': 300,
	},
	{
		'anchorId': 3,
		'x': 240,
		'y': 400,
	},
	{
		'anchorId': 4,
		'x': 480,
		'y': 100,
	},
	{
		'anchorId': 5,
		'x': 480,
		'y': 200,
	},
	{
		'anchorId': 6,
		'x': 480,
		'y': 300,
	},
	{
		'anchorId': 7,
		'x': 480,
		'y': 400,
	},
]

@app.route("/")
def root():
	return app.send_static_file('index.html')

@app.route("/get_anchors")
def GetAnchors():
	return jsonify(anchors)

@socketio.on('connect')
def Connect():
	print('Connected to client socket')


if __name__ == "__main__":
	# Dispatch the Flask app on another thread to handle
	# HTTP requests in the background while computation and
	# data collection run on main thread
	thread = threading.Thread(
		target=socketio.run, args=(app,),
		kwargs={'use_reloader': False}
	)
	thread.start()

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
