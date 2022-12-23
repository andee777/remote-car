var sketch = (p) => {

let xpos, ypos; // Starting position of shape

let xspeed = 18.8; // Speed of the shape
let yspeed = 2.2; // Speed of the shape

let xdirection = 1; // Left or Right
let ydirection = 1; // Top to Bottom
let carVector; 

  p.setup = () => {
    var c = p.createCanvas(document.getElementById('sketchContainer').offsetWidth, 400);
    p.background(51);
    p.strokeWeight(20);
    p.stroke(255, 100);
    xpos = p.width / 2;
    ypos = p.height / 2;
    carVector = new p5.Vector(xpos , ypos);
  };

  p.windowResized = () => {
    p.resizeCanvas(document.getElementById('sketchContainer').offsetWidth, 400);
    x = p.width / 2;
    y = p.height / 2;
    //dragSegment(current_x, current_y);
  };


  p.draw = () => {
    //p.clear();
    
    p.stroke(255);
    p.point(xpos , ypos);

    var axis0Val = parseFloat(document.getElementById("axis0").value);
    var axis1Val = parseFloat(document.getElementById("axis1").value);

    if(axis1Val != null) {
        if (axis1Val < 0.1 && axis1Val> -0.1) {
          axis1Val  = 0;
        }
    }

    if(axis0Val != null) {        
	if (axis0Val < 0.1 && axis0Val> -0.1) {
          axis0Val  = 0;
        }
    }

    // Update the position of the shape
    xpos = xpos + (xspeed * axis0Val * xdirection);
    ypos = ypos + (yspeed *axis1Val * ydirection);

  };


};
new p5(sketch, 'sketchContainer');
