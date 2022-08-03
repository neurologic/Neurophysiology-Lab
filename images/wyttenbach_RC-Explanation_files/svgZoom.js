// REDO this in a simpler way, following the way it's done in svgPlotOLD.js in test/scripts and current svgPlot.js

// redone to work as a script in html page that has inline svg.
// It now appears to also work when linked into an svg file that is linked to a page in an object tag!
// any part of any svg could have classes 'layer' 'zoom' 'plot' and will get the appropriate event listeners
// no layer events, but I could put the layer code in here to keep it together
// no plot events yet; they may go in a separate js file

// This currently depends on resize.js to handle window resizing, with the svg having a fixed pixel size.
// We get smoother resizing by setting (in css) #fig { width:100%; height:100%; }
// However, that no longer allows zoom to zoom into the mouse location, probably because s.getAttribute('width') returns '100%' instead of a number
// This may now be fixed by adjusting GetResize (new calculation of w) and getEventPoint (modify p if svg isn't at 0)
//
// WOULD LIKE to have some elements NOT scale so rapidly (e.g. labels and arrowheads)
// There's code to do this to text only, by changing font size at a slower rate than the zoom scale
// However, it only works if there is just one zooming area in fig and all parts can zoom.
// To extend it can't have <text> in <defs> but must be directly in zoom group.
// To do this using scaling (thus affecting non-text), I need to adjust location while maintaining
// rotation and rotation origin. That seemed like too much trouble.
// Could easily extend this approach to line-width. (vector-effect:non-scaling-stroke will do it but might want to scale more slowly rather than not at all)
// for arrowheads etc., use a font. Some useful ones: &bigstar; &cir; &star; &starf; &xcirc; &#x27A4; (right arrowhead)
// see https://html.spec.whatwg.org/multipage/named-characters.html#named-character-references
// https://mothereff.in/html-entities to create codes for characters



var gFigureMargin = 8; // used in getResize

window.addEventListener('DOMContentLoaded', initializeSVGzoom, false);


function initializeSVGzoom() { // DOMContentLoaded
	addEventHandlersSVGzoom(); // add behaviors to selected classes
}


function addEventHandlersSVGzoom() {
	// all elements that can zoom/pan need the mouse and scroll events
	var items = document.querySelectorAll('svg .zoom');
	for (var i = 0; i < items.length; i++) {
		items[i].addEventListener('dblclick',restoreHome);
		items[i].addEventListener('mouseup',zoomMouseUp);
		items[i].addEventListener('mousedown',zoomMouseDown);
		items[i].addEventListener('mousemove',zoomMouseMove);
		items[i].addEventListener('mouseout',zoomMouseOut);
		items[i].addEventListener('wheel', zoomMouseWheel, false);
		// not yet panning
		items[i].savePan = 0;
		// stored for later retrieval
		items[i].setAttribute('transform','matrix(1 0 0 1 0 0)'); // just define it with no transformation
		items[i].saveStateOrigin = parentSVGNode(items[i]).createSVGPoint();
		items[i].saveStartMatrix = parentSVGNode(items[i]).createSVGMatrix();
		items[i].saveStateTransform = parentSVGNode(items[i]).createSVGMatrix();
		// default cursor (or we get the I-beam over text items (do it here for svg that links the script)
		items[i].farthestViewportElement.setAttribute('cursor','default');
	}
	// save text font sizes with each text element
	saveTextSizes(document.getElementById('fig'));
	saveStrokeSizes(document.getElementById('fig'));
}

function restoreHome(e) {
	parentZoomGroup(e).setAttribute('transform','matrix(1 0 0 1 0 0)');
	// could instead set the transform baseVal
	setTextSizes(parentZoomGroup(e),1);
	setStrokeSizes(parentZoomGroup(e),1);
}



function saveTextSizes(g) {
//	var items = g.getElementsByTagName('text');
	var items = g.querySelectorAll('text.nozoom, .nozoom text');
	for (var i = 0; i < items.length; i++) {
		var fs = window.getComputedStyle(items[i]).fontSize.slice(0,-2);
		items[i].setAttribute('data-fontSize',fs);
	}
}
function setTextSizes(g,z) {
	g = document.getElementById('fig')
//	var items = g.getElementsByTagName('text');
	var items = g.querySelectorAll('text.nozoom, .nozoom text');
	for (var i = 0; i < items.length; i++) {
		var fs = items[i].getAttribute('data-fontSize');
		items[i].style.fontSize = (fs/z)+'px';
	}
}


function saveStrokeSizes(g) {
	var items = g.querySelectorAll(':not(text):not(g).nozoom, .nozoom :not(text)');
	for (var i = 0; i < items.length; i++) {
		var sw = window.getComputedStyle(items[i]).strokeWidth.slice(0,-2);
		items[i].setAttribute('data-stroke',sw);
	}
}
function setStrokeSizes(g,z) {
	g = document.getElementById('fig')
	var items = g.querySelectorAll(':not(text):not(g).nozoom, .nozoom :not(text)');
	for (var i = 0; i < items.length; i++) {
		var sw = items[i].getAttribute('data-stroke');
		items[i].style.strokeWidth = (sw/z)+'px';
	}
}


// amount of window-resize scaling
function getResize(s) {
	// s is now event.target.nearestViewportElement rather than the outermost one; we need the outermost one
	if (s.farthestViewportElement) s = s.farthestViewportElement; // in case there are sub-svg in the doc
	// offsetWidth and clientWidth are 0 and undefined, respectively
	var w = window.innerWidth-2*gFigureMargin; // Works for 100% OR px width with a single svg. With 2 svg, only the leftmost one stays centered on zoom
	// RE the above, there seems to be no way to get the actual size of any viewport other than the outermost one.
	// Also RE the above, WebKit works on both svg of a pair, FF works only on the leftmost one. This is true whether using
	var w0 = s.getAttribute('viewBox').split(' ')[2]; // width of the viewBox remains constant
	return parseFloat(w)/parseFloat(w0);
}


function getEventPoint(evt) {
	// evt.offsetX and evt.offsetY don't work in all browsers, so calculate it myself
//	return getEventPointFF(evt); // replicates evt.offsetX and evt.offsetY

	if (browserType() == 'Firefox') {
		return getEventPointFF(evt); // replicates evt.offsetX and evt.offsetY
	}
	// return the location of mouse inside the svg element
	var s = parentSVGNode(evt.target); // nearest svg element
	var p = s.createSVGPoint();
	// offsetX should give the location within a transformed (even rotated) svg
	// https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/offsetX
	// tested and working in Chrome and Safari, not in Firefox
	p.x = evt.offsetX;
	p.y = evt.offsetY;
	return p;
}


function getEventPointFF(evt) {
	// return the location of mouse inside the svg element
	var s = parentSVGNode(evt.target); // nearest svg element
	var p = s.createSVGPoint();
	// get window size, amount of window resizing, and current zoom scale
	var w = s.getBBox().width, h = s.getBBox().height;
	var rz = getResize(s);
	var g = document.getElementsByClassName('zoom')[0]
	var scale = g.transform.baseVal[0].matrix.a;
	// adjust the window width accordingly
	w *= rz/scale; h *= rz/scale;

	// location of the mouse in the image
	var x = evt.pageX-gFigureMargin, y = evt.pageY-gFigureMargin;

	// find the user-imposed rotation and adjust x and y from the appropriate corner
	var list = document.getElementById('fig').classList;
	if (list.contains('r90')) {p.x = y; p.y = w - x;}
	else if (list.contains('r180')) {p.x = w - x; p.y = h - y;}
	else if (list.contains('r270')) {p.x = h - y; p.y = x;}
	else {p.x = x; p.y = y;}

	return p;
}


function parentZoomGroup(evt) {
	// get the first parent node of class 'zoom'
	if (evt.currentTarget) return evt.currentTarget; // Gets the node with the event listener; good in FF, null in WK where we need it
	var node = actualNode(evt.target);
	// climb up to the first node with class 'zoom'
	while (node && node.className.baseVal.indexOf('zoom') < 0) node = node.parentNode;
	return node;// null if no node is found
}


function parentSVGNode(node) {
	node = actualNode(node);
	return node.nearestViewportElement;
}


function actualNode(node) {
	if (node.nodeType == 3) node = node.parentElement; // if a text node, get its parent SVGTextElement (Safari reports text nodes)
	if (node.nodeName == 'tspan') node = node.parentElement;
	if (node.correspondingUseElement) node = node.correspondingUseElement; // for WebKit, move away from <def> to the used element
	return node;
}


/**
 * Sets the current transform matrix of an element.
 */
function setCTM(g,m) {
	g.transform.baseVal[0].setMatrix(m);
	return;
}


function zoomMouseWheel(evt) {
	if(evt.preventDefault) evt.preventDefault();
	evt.returnValue = false;
	// get the svg document targeted by this event
	var g = parentZoomGroup(evt);
	if (!g) return; // clicked on something that wasn't part of a zoom group
	var svgDoc = parentSVGNode(g);

	// determine the amount by which to zoom (z)
	var zoomScale = 1.2; // Zoom sensitivity
	var delta = -evt.deltaY/300; // sign * Math.max(Math.abs(e.deltaX),Math.abs(e.deltaY))
	var z = Math.pow(zoomScale,delta);
	if (evt.scale) z = evt.scale; // iOS gesture
	// When the svg is resized via setting its width and height attributes, the CTM is affected but the transform attribute is not.
	// thus the ctm might be 1.1 0 0 1.1 0 0 while the transform is 1 0 0 1 0 0
	// (this happens when the html specifies a size other than original or when the user resizes a window)

	// determine how much the svg has been resized (either in the svg tag or by the user resizing)
	var resize = getResize(svgDoc);

	// current transformation independent of window resizing (NOT getCTM(), which reflects window size changes)
	var m = g.transform.baseVal[0].matrix;
	// determine where the user clicked and correct for resizing of the image
	var p = getEventPoint(evt); // point within the viewing area

	p.x /= resize; p.y /= resize; // correct for window resizing
	p = p.matrixTransform(m.inverse()); // account for any prior translation of the image

	// calculate the needed transformtion: move the origin to p, scale, and move the origin back
	var k = svgDoc.createSVGMatrix().translate(-p.x*(z-1),-p.y*(z-1)).scale(z);
	var newCTM = m.multiply(k);
	// constrain to keep the image in its bounding area and not scaled too small, then apply the transformation
	newCTM = constrainCTM(g,newCTM);
	setCTM(g,newCTM);

	// compensate in order to keep text the same size if they have class 'nozoom'
	if (newCTM.a >= 1) adjustFontAndStrokeSize(svgDoc,g,newCTM.a); // could send newCTM.a as a parameter

	// update the stateTf in case we're zooming while panning (mousedown, wheel while dragging, mouseup)
	if (!g.savePan) return; // not panning
	g.saveStateTransform.multiply(k.inverse());
}


function zoomMouseMove(evt) {
	if(evt.preventDefault) evt.preventDefault();
	evt.returnValue = false;

	var g = parentZoomGroup(evt);
	if (!g) return; // over something that wasn't part of a zoom group

	if(g.savePan) { // Pan mode
		var svgDoc = parentSVGNode(g);
		var stateTf = g.saveStateTransform;
		var stateOrigin = g.saveStateOrigin;
		var p = getEventPoint(evt);
		var resize = getResize(svgDoc);
		p.x /= resize; p.y /= resize;
		p = p.matrixTransform(stateTf);
		var newCTM = stateTf.inverse().translate(p.x - stateOrigin.x, p.y - stateOrigin.y);
		newCTM = constrainCTM(g,newCTM);
		setCTM(g,newCTM);
	}
}


function constrainCTM(g,newCTM) {
	// don't scale smaller than the view area
	var startMatrix = g.saveStartMatrix;
	if (newCTM.a < startMatrix.a) return startMatrix;
	// don't pull the left top into view
	newCTM.e = Math.min(newCTM.e,0);
	newCTM.f = Math.min(newCTM.f,0);
	// don't pull the right bottom into view either
	newCTM.e = Math.max(newCTM.e,g.getBBox().width*(1-newCTM.a));
	newCTM.f = Math.max(newCTM.f,g.getBBox().height*(1-newCTM.a));
	return newCTM;
}


function zoomMouseDown(evt) {
	if(evt.preventDefault) evt.preventDefault();
	evt.returnValue = false;

	var g = parentZoomGroup(evt);
	if (!g) return; // clicked on something that wasn't part of a zoom group
	var svgDoc = parentSVGNode(g);

	// start panning
	g.savePan = 1;

	// account for window resizing
	var resize = getResize(svgDoc);

	// set the point of origin and the inverse transformation state for use during panning
	var stateTf = g.transform.baseVal[0].matrix.inverse();
	var p = getEventPoint(evt);
	p.x /= resize; p.y /= resize;
	g.saveStateOrigin = p.matrixTransform(stateTf);
	g.saveStateTransform = stateTf;
}


function zoomMouseUp(evt) {
	if(evt.preventDefault) evt.preventDefault();
	evt.returnValue = false;
	var g = parentZoomGroup(evt);
	if (!g) { window.opener.console.log('mouseup with !g',evt); return;} // clicked on something that wasn't part of a zoom group
	g.savePan = 0;
}


function zoomMouseOut(evt) {
	// act as mouseOut only when the cursor moves out of the 'window' (SVG object), not when it moves over another object in the svg.

	if(evt.preventDefault) evt.preventDefault();
	evt.returnValue = false;

	// this next test may not be needed - the redone parentZoomGroup() may catch it.
	// THIS HAPPENS FREQUENTLY. Now remove it and see if g test catches it
	var p = getEventPoint(evt);
	if (p.x >= 0 && p.x <= window.innerWidth && p.y >= 0 && p.y <= window.innerHeight) return; // still inside the svg

	// left the svg
	var g = parentZoomGroup(evt);
	if (!g) { window.opener.console.log('mouseout with !g',evt); return;} // clicked on something that wasn't part of a zoom group NEVER HAPPENS
	g.savePan = 0;
}



///////// Allow text to not scale (for text, could allow to scale to some maximum size?)
/*
This approach works ONLY if there is just one zooming figure and if all parts of that figure can zoom.
To work with multiple zooming areas, I can't have text in <defs> and must use zoom group rather than fig as svgDoc in this code
Use &#x27A4; as a non-scaling arrowhead pointer

I could have different zoom levels designated by class:
zoom-10 for no zooming, zoom-0 for normal zooming; current is like zoom-6 for text, zoom-3 for lines
thus text grows more slowly than lines

*/

function adjustFontAndStrokeSize(svgDoc,zoomGroup,zoom) {
	var adjust = Math.pow(zoom,0.6);
	var items = svgDoc.querySelectorAll('text.nozoom, .nozoom text');
	for (var i = 0; i < items.length; i++) {
		var fs = items[i].getAttribute('data-fontSize');
		fs = fs/adjust;
		items[i].style.fontSize = fs+'px';
	}
	var adjust = Math.pow(zoom,0.3);
	var items = svgDoc.querySelectorAll(':not(text):not(g).nozoom, .nozoom :not(text)');
	for (var i = 0; i < items.length; i++) {
		var sw = items[i].getAttribute('data-stroke');
		sw = sw/adjust;
		items[i].style.strokeWidth = sw+'px';
	}
}


