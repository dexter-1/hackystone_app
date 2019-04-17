const radius = 10;
const fontsize = 11;
const localhost = 'http://192.168.43.139:5000';


const dimX = 550;
const dimY = 200;
let getTags = null;

function setup() {
	// initialize socket conenction with the server
	const socket = io.connect(localhost);

	// draw canvas
	const canvas = createCanvas(dimX, dimY);
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

				if (anchors[i].X == 0) {
					anchors[i].X += 5;
				} else if(anchors[i].X == dimX) {
					anchors[i].X -= 5;
				}			
				
				if (anchors[i].Y == 0) {
					anchors[i].Y += 5;
				} else if(anchors[i].Y == dimY) {
					anchors[i].Y -= 5;
				}	

				circle(anchors[i].X, anchors[i].Y, radius);
				fill(255);
				textAlign(CENTER);
				text('Anchor ' + anchors[i].anchorId, anchors[i].X, anchors[i].Y - 10);
			}
		}
	}
	http.open('GET', '/get_anchors', true);
	http.send(null);

	// socket event handler to get tags
	function tagOnReadyStateChange() {
		if (getTags.readyState == 4 && getTags.status == 200) {
			tag = JSON.parse(getTags.responseText);
			background(0);

			for (let i = 0; i < anchors.length; i++) {
				// put in anchor points onto the canvas
				fill(255,0,0);
				circle(anchors[i].X, anchors[i].Y, radius);

				fill(255);
				textAlign(CENTER);
				text('Anchor ' + anchors[i].anchorId, anchors[i].X, anchors[i].Y - 10);
			}
			
			tag.X = max(2, tag.X);
			tag.X = min(dimX - 2, tag.X);
			tag.Y = max(2, tag.Y);
			tag.Y = min(dimY - 2, tag.Y);

			fill(255);
			circle(tag.X, tag.Y, radius);

			fill(255);
			textAlign(CENTER);
			text('Tag ' + tag.tagId, tag.X, tag.Y - 10);
		}
	}

	function main() {
		getTags = new XMLHttpRequest();
		getTags.onreadystatechange = tagOnReadyStateChange;
		getTags.open('GET', '/get_tags', true);
		getTags.send(null);
		setTimeout(main, 1000);
	};

	main();
}
