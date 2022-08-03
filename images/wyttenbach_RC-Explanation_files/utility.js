// Crawdad utilities

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-26187529-37', 'auto');
ga('send', 'pageview');


function arrayMinMax(a) {
	var min = Infinity;
	var max = -Infinity;
	for(var i = 0; i < a.length; i++) {
		min = a[i] < min ? a[i] : min;
		max = a[i] > max ? a[i] : max;
	}
	return { min:min, max:max }
}

function removeDuplicates(a) {
	return [...new Set(a)];
}

function getCSSVariable(name) {
	return getComputedStyle(document.body).getPropertyValue(name);
}
function setCSSVariable(name,value) {
	document.body.style.setProperty(name,value);
}


function openFigureWindow(figURL) {
	// if the window exists, get a reference to it
window.open(figURL,'_blank');
return;
	var abbrevURL = shortURL(figURL);
	var size = getFigureWindowSize(abbrevURL);
console.log('openfigurewindow',size);
	if (!size[0]) size[0] = 600;
	if (!size[1]) size[1] = 400;
	// KLUDGE (search all source for KLUDGE to find ugly stuff that I hope to remove later)
	// try this to make Android open videos in a new tab instead of in a pseudo-window where video can't go fullScreen
	if (navigator.appVersion.toLowerCase().indexOf('android') > -1 && (abbrevURL.indexOf('vid.') > -1 || fig.toLowerCase().indexOf('test') > -1)) {
		//alert('openFigureWindow  android');
		//console.log('android');
		var w = window.open(figURL,cleanName(abbrevURL)); // this is what we want for Android
	} else {
		//alert('openFigureWindow not android');
		//console.log('not android');
		var w = window.open('',cleanName(abbrevURL),'width='+size[0]+',height='+size[1]+',toolbar=0,resizable=1,scrollbars=0,status=0,menubar=0,links=0,location=0,navigation=0,directories=0'); // this is what we want for desktop and iOS
	}
	// When w has location 'about:blank', Chrome allows the next bit and reports 'blank'
	// On subsequent calls with the window already open, Chrome complains that accessing w.location is 'unsafe' and just gives w the focus.
	// This isn't clean, but it has the desired effect.
	if (w.location.href == 'about:blank') w.location = figURL;
	w.focus(); // this may be redundant, since window.open probably already does it.
	return w;
}


function adjustForWindows() {
	if (window.navigator.platform.indexOf('Win') < 0) return;
	var items = document.querySelectorAll('input[type="radio"], input[type="checkbox"], button, .showmval, showpval');
	for (var i = items.length-1; i >= 0; i--) items[i].classList.add('win');

	// get rid of the ugly border that IE puts on all iframes
	// because there can be a small lag, it may be best to put this in the html directly, even though it won't validate as html5
	var items = document.querySelectorAll('iframe');
	for (var i = items.length-1; i >= 0; i--) {
		items[i].setAttribute('frameborder','0');
		items[i].setAttribute('allowtransparency','true');
		items[i].outerHTML = items[i].outerHTML; // required for IE to actually make the change
		//alert(i+' '+items[i].frameBorder+' '+items[i].allowTransparency);
	}

	// if the browser is one that messes up {height:100%} on svg figures, make it remove the height designation altogether
	// It will not enlarge the figure when the window expands, but at least it will display it at the right initial size.
	// see #figbody:not(.svgheightbug) #fig and #figbody:.svgheightbug #fig in manual.css for the height styling.
	var browser = browserType();
	if (browser == 'MSIE' || browser == 'Safari' || browser == 'MSIE10') {
		items = document.querySelectorAll('#figbody')[0].classList.add('svgheightbug'); // MSIE doesn't recognize className or classList on svg objects,
	}
}

var gSpace; // if not defined, this will give an error
var gMilli;

function formatSIU(val,forceMilli) {
	// val is a number that may need an SIU suffix in n, mu (u), m, k, or M
	if (forceMilli == undefined) forceMilli = gMilli;

	if (isNaN(val)) return '&nbsp;';
	if (val == 'error') return 'error';
	if (val == 0) return '0';
	var sign = val * Math.abs(val); ////////// WHY? Why not just check whether num < 0
	var num = Math.abs(val)
	var mult = 0
	while (num >= 1000) {
		num /= 1000;
		mult += 3;
	}
	if (forceMilli) {
		// show 0.9 as 900m
		while (num < 1) { // changed from <= to < on 4/26/16
			num *= 1000;
			mult -= 3;
		}
	} else {
		// show 0.9 as 0.9
		while (num <= 0.1) {
			num *= 1000;
			mult -= 3;
		}
	}
	var siu = ''
	if (mult == -12)
		siu = 'p';
	else if (mult == -9)
		siu = 'n';
	else if (mult == -6)
		siu = 'µ';
	else if (mult == -3)
		siu = 'm';
	else if (mult == 3)
		siu = 'k';
	else if (mult == 6)
		siu = 'M';
	else if (mult == 9)
		siu = 'G';
	else if (mult == 12)
		siu = 'T';

	var s = num.toString();
	if (s.length > 3) s = num.toPrecision(3);

	if (gSpace) siu = ' ' + siu;

	/*if (sign < 0)*/if (val < 0)
		return '-' + s + siu;
	else
		return s + siu;
}


function unformatSIU(val) {
	// val is a number that may end in n, mu (u), m, k, or M
	// turn it into a real value
	if (isFinite(val)) return parseFloat(val); // no unit prefix
	//if (isFinite(parseFloat(val))) return parseFloat(val); // no unit prefix IT TURNS OUT that parseFloat("1.2m") gives 1.2 now!
	val = val.split(" ").join();
	//val = val.replace(/\s*/g, " "); // remove spaces first
	var u = val.substring(val.length-1); // get unit prefix
	var num = parseFloat(val.substring(0,val.length-1)); // get rest of number
	if (!isFinite(num)) return 0; // if invalid return zero to prevent NaN problems later?
	num = eval(num);

	if (u == "p")
		num /= 1000000000000;
	else if (u == "n")
		num /= 1000000000;
	else if (u == "u")
		num /= 1000000;
	else if (u == "µ")
		num /= 1000000;
	else if (u == "m")
		num /= 1000;
	else if (u == "k")
		num *= 1000;
	else if (u == "M")
		num *= 1000000;
	else if (u == "G")
		num *= 1000000000;
	else if (u == "T")
		num *= 1000000000000;
	else
		num = num;

	return num;
}


function cleanName(s) {
	return s.replace(/[\W]/g,'_');
}


function debug(how) {
	var a = [];
	// ie9 displays an array with no spaces between elements, so for testing there, must use s instead of a in console.log
	for (var i = 1; i < arguments.length; i++) a[i-1] = arguments[i];
	var s = a.join(', ');
	if (how.indexOf('a') ==0) { // a for alert
		alert(s);
	} else if (how.indexOf('w') == 0) { // w for opener window
		if (browserType() == 'Chrome' || !window.opener || !window.opener.console) {
			console.log(s);
		} else {
			window.opener.console.log(s);
		}
	} else { // c for console
		console.log(s);
	}
}


function browserType() {
	var ua = navigator.userAgent;
	if (ua.indexOf('Edge') >= 0) return 'Edge'; // test this first because it also says Chrome and Safari!
	if (ua.indexOf('OPR') >= 0) return 'Opera'; // test this first because it also says Chrome and Safari!
	if (ua.indexOf('Chrome') >= 0) return 'Chrome'; // test this next because it also says Safari
	if (ua.indexOf('Safari') >= 0) return 'Safari'; // only test this after testing Opera and Chrome
	if (ua.indexOf('MSIE 10') >= 0) return 'MSIE10'; // version 10
	if (ua.indexOf('Trident') >= 0) return 'MSIE'; // version 11 no longer identifies itself as MSIE
	if (ua.indexOf('Firefox') >= 0) return 'Firefox';
	return '';
}


///////////////////////////// links //////////////////////////////



// NOTE THIS WILL ALSO NEED TO BE DONE IN FIGURE WINDOWS in case they have links to other figures

function replaceTextLinks() {
	// look at the href, get the base name of the file, and then look up its short and long titles
	// put long title in the innerHTML of the link. For example:
	//<a href='7.StretchReceptor/vid.7.1.html' class='fig'>Video 7.1, MRO Dissection and Recording</a>
	var items, i, theTitle;

	var t = new Date;
	var ms = t.getMilliseconds();

	items = document.querySelectorAll('a.fig');
	for (i = items.length-1; i >= 0; i--) {
		theTitle = getTitles(shortURL(items[i].href));
		if (!theTitle) continue; // GetFigureTitle can return null or undefined if figName isn't found
		if (theTitle[0].length) {
			items[i].innerHTML = theTitle[0]+', '+theTitle[2]; // number and full title, e.g. Video 7.1, MRO Dissection and Recording
		} else {
			items[i].innerHTML = theTitle[2]; // Saline Calculator doesn't have an equation number
		}
	}

	t = new Date;
//	console.log('replaceTextLinks',items.length,t.getMilliseconds()-ms); // takes 1 ms for 18 links in lab 7
	// also need to do it for lab links
}


function shortURL(url) {
	return (url.split('/').pop().split('.html')[0]).toLowerCase();
}

function giveFigureTitles() {
	// title of the window, caption heading; this is done in figure and video windows
}



///////////////////////////// saving figures //////////////////////////////

function svgToLink(id) {
	return 'data:image/svg;base64,'+svgToBase64(id);
	// create a link with href=svgToLink('fig') to save as a data file
}

function svgToClip(id) {
 // not clear what to put here
 // could create an img tag and set its data to the base64 encoded SVG and then copy that
 // see https://stackoverflow.com/questions/12255444/copy-svg-images-from-browser-to-clipboard
 // per the above, <img src="data:image/svg;base64,theEncodedSVGtext" can be copied right-clicked, etc.
 // however, it's not clear how to set MIME type for clipboard.
}


function svgToBase64(id) {
	var t = document.getElementById(id).outerHTML;
	//return btoa(t);
	return base64EncodeUnicode(t);
}


function base64EncodeUnicode(str) {
	// First we escape the string using encodeURIComponent to get the UTF-8 encoding of the characters,
	// then we convert the percent encodings into raw bytes, and finally feed it to btoa() function.
	utf8Bytes = encodeURIComponent(str).replace(/%([0-9A-F]{2})/g, function(match, p1) {
		return String.fromCharCode('0x' + p1);
	});
	return btoa(utf8Bytes);
}







