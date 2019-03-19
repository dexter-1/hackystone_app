const radius = 2;
const fontsize = 8;
const localhost = 'http://localhost:5000';

function setup() {
	// initialize socket conenction with the server
	const socket = io.connect(localhost);

	// draw canvas
	const canvas = createCanvas(720, 500);
	textSize(fontsize);
	canvas.parent('canvas-holder');
	background(0);
	noFill();

	let anchors;

	// request to get anchor positions
	const http = new XMLHttpRequest();
	http.onreadystatechange = function() {
		if (http.readyState == 4 && http.status == 200) {
			anchors = JSON.parse(http.responseText);

			for (let i = 0; i < anchors.length; i++) {
				// put in anchor points onto the canvas
				fill(255,0,0);
				circle(anchors[i].x, anchors[i].y, radius);

				fill(255);
				textAlign(CENTER);
				text('Anchor ' + anchors[i].anchorId, anchors[i].x, anchors[i].y - 10);
			}
		}
	}
	http.open('GET', '/get_anchors', true);
	http.send(null);

	// socket event handler to get tags
	socket.on('tags',
		function(tag) {
			background(0);

			for (let i = 0; i < anchors.length; i++) {
				// put in anchor points onto the canvas
				fill(255,0,0);
				circle(anchors[i].x, anchors[i].y, radius);

				fill(255);
				textAlign(CENTER);
				text('Anchor ' + anchors[i].anchorId, anchors[i].x, anchors[i].y - 10);
			}

			fill(255);
			circle(tag.x, tag.y, radius);

			fill(255);
			textAlign(CENTER);
			text('Tag ' + tag.tagId, tag.x, tag.y - 10);
		}
	);
}
