window.addEventListener('DOMContentLoaded', initializeFigure, false);

window.gLabel = true; // show labels by default
window.gLayer; // currently shown layer


function initializeFigure() {
	adjustForWindows(); // also checks for MSIE/Safari and adjusts svg display accordingly
	addEventHandlersFigure(); // add behaviors to selected classes
	setInitialState();  // rotation status, if any
	displayLayers(window.location.hash.substr(1)); // initial layer setup, if there are layers

//	console.log('init',window.innerHeight,document.getElementById('figbody').offsetHeight);
}


function addEventHandlersFigure() {
	// figure links call ShowFigure and suppress the href link
	var items = document.querySelectorAll('a.fig');
	for (var i = items.length-1; i >= 0; i--) items[i].addEventListener('click',showFigure,false);

	// svg control info
	items = document.getElementById('svgcontrol');
	if (items) {
		items.addEventListener('mouseover',showSVGInstruct,false);
		items.addEventListener('mouseout',hideSVGInstruct,false);
	}

	// label controls
	items = document.getElementById('hidelabels');
	if (items) items.addEventListener('click',hideLabels,false);
	items = document.getElementById('showlabels');
	if (items) items.addEventListener('click',showLabels,false);

	// layer controls
	items = document.querySelectorAll('a.layer');
	for (var i = items.length-1; i >= 0; i--) items[i].addEventListener('click',showLayer,false);

	// rotation controls
	items = document.querySelectorAll('a.setrotation');
	for (var i = items.length-1; i >= 0; i--) items[i].addEventListener('click',rotateImage,false);
	// rotation controls
	items = document.querySelectorAll('a.advancerotation');
	for (var i = items.length-1; i >= 0; i--) items[i].addEventListener('click',nextRotation,false);

	// toggle controls
	items = document.querySelectorAll('a.toggle');
	for (var i = items.length-1; i >= 0; i--) items[i].addEventListener('click',toggleLayer,false);
	items = document.querySelectorAll('a.toggleclass');
	for (var i = items.length-1; i >= 0; i--) items[i].addEventListener('click',toggleClass,false);


//	window.addEventListener('resize',resizeFigure);

//	resizeFigure();
}


function setInitialState() {
	// allow a link to set the body class (e.g. He/Ly)
	//if (window.location.hash) document.body.classList.add(window.location.hash.slice(1));
	var hash = window.location.hash.slice(1).split(',');
	var fig = document.getElementById('fig');
	for (var i = 0; i < hash.length; i++) {
		if (hash[i] == 'r0' || hash[i] == 'r90' || hash[i] == 'r180' || hash[i] == 'r270') {
			fig.classList.add(hash[i]);
			console.log(i,hash[i],fig.classList);
		} else if (hash[i]) {
			document.body.classList.add(hash[i]);
			console.log(i,hash[i]);
		}
	}

	// initial rotation state
	if (fig.classList.contains('r0')) doRotation(0); // probably not necessary
	if (fig.classList.contains('r90')) doRotation(90);
	if (fig.classList.contains('r180')) doRotation(180);
	if (fig.classList.contains('r270')) doRotation(270);
}


function resizeFigure() {
	const b = document.body;
	const f = document.getElementById('fig');
	var w, h;
	switch (f.nodeName) {
		case 'svg' :
			w = f.width.animVal.value; h = f.height.animVal.value;
			break;
		case 'img' :
			w = f.width; h = f.height;
			break;
		case 'table' :
			w = f.width; h = f.height;
			break;
		case 'form' :
			w = f.width; h = f.height;
			break;
	}
	console.log(b.offsetWidth,b.offsetHeight,w,h,fig.clientWidth,fig.clientHeight);
	// for now, leave table and form alone. Could also leave img alone or force it to stay at its natural width or under

}



function showSVGInstruct() {
	var items = document.getElementById('svginstruct');
	if (items) items.classList.add('show');
}


function hideSVGInstruct() {
	var items = document.getElementById('svginstruct');
	if (items) items.classList.remove('show');
}


// to open new figure windows from links in the caption
// this is the same function that is present in figure.js and manual.js
function showFigure(evt) {
	evt.preventDefault(); // don't go to the url
	var w = openFigureWindow(this.href); // in utility.js
	w.moveBy(24,24); // or it overlaps the current window
	return false;
}


// show the desired initial state
function displayLayers(layerName) {
	if (layerName.length < 1) layerName = document.getElementById('fig').getAttribute('data-layer');
	if (!layerName) return; // no layers in this figure
	setLayer(layerName);
	// by default, labels are shown, so don't bother with an attribute for it
	setLabels(true);
}


function setLayer(layerName) {
	// this method permits different numbers of layers, labels, and captions (e.g. one caption for all)
	var fig = document.getElementById('fig'); //.contentDocument; // fails in Chrome due to 'security'; will work only if svg is inline
	// hide all layers and then show the selected one
	var items = fig.querySelectorAll('.layer');
	if (!items.length) return;
	window.gLayer = layerName;
	for (var i = 0; i < items.length; i++) items[i].setAttribute('visibility','hidden');
	fig.querySelector('.layer.'+layerName).setAttribute('visibility','visible');
	// hide all labels and show the selected one (no need if layers are already hidden)
	if (window.gLabel) {
		items = fig.querySelectorAll('.label');
		for (i = 0; i < items.length; i++) items[i].setAttribute('visibility','hidden');
		items = fig.querySelector('.label.'+layerName);
		if (items) items.setAttribute('visibility','visible');
	}
	// hide all but the desired layer caption
	items = document.querySelectorAll('span.layer');
	for (i = 0; i < items.length; i++) items[i].style.display = 'none';
	items = document.querySelectorAll('span.layer.'+layerName);
	for (i = 0; i < items.length; i++) items[i].style.display = 'inline';
}



function toggleLayer(evt) {
	evt.preventDefault();
	layerName = this.hash.substr(1);
	// Toggles visibility of anything with classes 'layer' and 'layerName'
	var fig = document.getElementById('fig'); //.contentDocument; // fails in Chrome due to 'security'; will work only if svg is inline
	// hide all layers and then show the selected one
	var items = fig.querySelectorAll('.layer.'+layerName);
	for (var i = 0; i < items.length; i++) items[i].setAttribute('visibility',items[i].getAttribute('visibility')=='hidden'?'visible':'hidden');
	return false;
}


function toggleClass(evt) {
	// toggle a class on the main body
	evt.preventDefault();
	var theClass = this.hash.substr(1); // #ly or #he etc.
	// Toggles theClass on and off
	document.body.classList.toggle(theClass);
	return false;
}

function swapClass(evt) {
	// swap classes on the main body
	evt.preventDefault();
	var theClass = this.hash.substr(1).split('-'); // #ly-he swaps ly for he
	// Swap them
	document.body.classList.add(theClass[0]);
	document.body.classList.remove(theClass[1]);
	return false;
}




function showLayer(evt) {
	evt.preventDefault();
	setLayer(this.hash.substr(1));
	return false;
}


function setLabels(onoff) {
	window.gLabel = !!onoff;
	var fig = document.getElementById('fig'); //.contentDocument; // fails in Chrome due to 'security'; will work only if svg is inline
	// just set the label for the current layer.
	var items = fig.querySelectorAll('.label.'+window.gLayer)
	for (var i = 0; i < items.length; i++) items[i].setAttribute('visibility',window.gLabel?'visible':'hidden');
	// and change the instructions accordingly
	items = document.querySelectorAll('#hidelabels, .hidelabels')
	for (i = 0; i < items.length; i++) items[i].style.display = window.gLabel ? 'inline' : 'none';
	items = document.querySelectorAll('#showlabels, .showlabels')
	for (i = 0; i < items.length; i++) items[i].style.display = window.gLabel ? 'none' : 'inline';
}


function showLabels(evt) {
	evt.preventDefault();
	setLabels(1);
	return false;
}


function hideLabels(evt) {
	evt.preventDefault();
	setLabels(0);
	return false;
}


function rotateImage(evt) {
	evt.preventDefault();
	var amt = this.hash.substr(1); // 0, 90, 180, 270
	doRotation(amt);
	return false;
}

function nextRotation(evt) {
	evt.preventDefault();
	var dir = this.hash.substr(1); // cw or ccw
	var list = document.getElementById('fig').classList;
	var n = 0;
	if (list.contains('r90')) n = 1;
	else if (list.contains('r180')) n = 2;
	else if (list.contains('r270')) n = 3;
	if (dir == 'cw') n++; else n--;
	if (n > 3) n = 0;
	if (n < 0) n = 3;
	doRotation([0,90,180,270][n]);
	return false;
}


function doRotation(amt) {
	var fig = document.getElementById('fig');
	fig.classList.remove('r0');
	fig.classList.remove('r90');
	fig.classList.remove('r180');
	fig.classList.remove('r270');
	fig.classList.add('r'+amt);
	var items = document.getElementsByTagName('text');
	var newAmt;
	for (var i = 0; i < items.length; i++) {
		if (items[i].classList.contains('keepHT')) {
			if (amt == 0) newAmt = 0;
			if (amt == 90) newAmt = 0;
			if (amt == 180) newAmt = 180;
			if (amt == 270) newAmt = 0;
		} else if (items[i].classList.contains('keepHB')) {
			if (amt == 0) newAmt = 0;
			if (amt == 90) newAmt = 180;
			if (amt == 180) newAmt = 180;
			if (amt == 270) newAmt = 180;
		} else if (items[i].classList.contains('keepVL')) {
			if (amt == 0) newAmt = 270;
			if (amt == 90) newAmt = 270;
			if (amt == 180) newAmt = 270;
			if (amt == 270) newAmt = 90;
		} else if (items[i].classList.contains('keepVR')) {
			if (amt == 0) newAmt = 90;
			if (amt == 90) newAmt = 270;
			if (amt == 180) newAmt = 90;
			if (amt == 270) newAmt = 90;
		} else if (items[i].classList.contains('letRotate')) {
			newAmt = 0;
		} else {
			newAmt = -amt;
		}
		var x = items[i].getAttribute('x');
		var y = items[i].getAttribute('y');
		items[i].setAttribute('transform','rotate('+newAmt+' '+x+','+y+')'); // OK
	}
	return false;
}

// for even better results, look at the anchor point of the text
// if text-anchor:middle, leave it alone
// if start
// if end
// for dominant-baseline:central, leave it alone
// if baseline
// if hanging
// YES, I need this if I use text arrowheads and have them not scale
// BUT what about text that's already rotated, like an arrowhead? Just let it rotate.
function doRotationNEW(amt) {
	var fig = document.getElementById('fig');
	fig.classList.remove('r0');
	fig.classList.remove('r90');
	fig.classList.remove('r180');
	fig.classList.remove('r270');
	fig.classList.add('r'+amt);
	var items = document.getElementsByTagName('text');
	var newAmt;
	for (var i = 0; i < items.length; i++) {
		if (items[i].classList.contains('keepHT')) {
			if (amt == 0) newAmt = 0;
			if (amt == 90) newAmt = 0;
			if (amt == 180) newAmt = 180;
			if (amt == 270) newAmt = 0;
		} else if (items[i].classList.contains('keepHB')) {
			if (amt == 0) newAmt = 0;
			if (amt == 90) newAmt = 180;
			if (amt == 180) newAmt = 180;
			if (amt == 270) newAmt = 180;
		} else if (items[i].classList.contains('keepVL')) {
			if (amt == 0) newAmt = 270;
			if (amt == 90) newAmt = 270;
			if (amt == 180) newAmt = 270;
			if (amt == 270) newAmt = 90;
		} else if (items[i].classList.contains('keepVR')) {
			if (amt == 0) newAmt = 90;
			if (amt == 90) newAmt = 270;
			if (amt == 180) newAmt = 90;
			if (amt == 270) newAmt = 90;
		} else if (items[i].classList.contains('letRotate')) {
			newAmt = 0;
		} else {
			newAmt = -amt;
		}
		var x = items[i].getAttribute('x');
		var y = items[i].getAttribute('y');
		if (!items[i].classList.contains('letRotate')) {
			items[i].setAttribute('transform','rotate('+newAmt+' '+x+','+y+')'); // OK
		}
	}
	return false;
}

/*
function reflectImage(evt) {
	evt.preventDefault();
	var how = this.hash.substr(1); // 0 or 1 (flip Y)
	doRotation(amt);
	return false;
}

function doReflection(how) {
	var fig = document.getElementById('fig');
	fig.classList.remove('r0');
	fig.classList.remove('r90');
	fig.classList.remove('r180');
	fig.classList.remove('r270');
	fig.classList.add('r'+amt);
	var items = document.getElementsByTagName('text');
	var newAmt = amt;
	for (var i = 0; i < items.length; i++) {
		var x = items[i].getAttribute('x');
		var y = items[i].getAttribute('y');
		// BUT I need to add this to whatever rotation may have occurred?
		items[i].setAttribute('transform','scale(1 '+x+','+y+')');
	}
	return false;
}
*/



/*
<p class='caption'>
<strong>Figure A.2.</strong>
<span class='layer methyleneblue'>Ventral view of a crayfish tail segment after dissection and staining with methylene blue. Note the ventral nerve cord (vnc), ganglia of the 3rd and 4th segments (g3, g4), nerves (n1, n2, n3), and the superficial flexor muscle (sf) with its attachment point (ma).</span>
<span class='layer janusgreen'>Ventral view of a crayfish tail segment after dissection and staining with Janus green. Note the ventral nerve cord (vnc), ganglia of the 3rd and 4th segments (g3, g4), nerves (n1, n2, n3), and the superficial flexor muscle (sf) with its attachment point (ma).</span>
<span class='layer dissected'>Ventral view of a crayfish tail segment after dissection but before staining. Note the ventral nerve cord (vnc), ganglia of the 3rd and 4th segments (g3, g4), nerves (n1, n2, n3), and the superficial flexor muscle (sf) with its attachment point (ma).</span>
<span class='layer undissected'>Ventral view of a crayfish tail segment before dissection. Anterior is up. Note the sternites of segments 3 and 4 (s3, s4) and the stumps of the swimmerets (sw). The superficial flexor muscle attaches to the skin at a line (ma).<br></span>
<br>Select an image:
<a href='#undissected' class='layer'>undissected</a>,
<a href='#dissected' class='layer'>dissected</a>,
<a href='#janusgreen' class='layer'>Janus green</a> stained,
<a href='#methyleneblue' class='layer'>methylene blue</a> stained.
Click to <a href='#hide' id='hidelabels'>remove labels</a><a href='#show' id='showLabels'>add labels</a>.</p>
*/
