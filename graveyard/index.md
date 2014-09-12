---
layout: page
title: Graveyard
---

<style type="text/css">

body {
	background: #000;
	background-image: none !important;
	color: #fff;
}

#quote, #quote a {
	color: #fff !important;
}

.graveyard {
	font-size: 200%;
	text-align: center;
	font-family: "Times New Roman", Georgia;
	text-shadow: 1px 0px 2px #aaa, -1px 0px 2px #aaa, 0px -1px 2px #aaa, 0px 1px 2px #aaa;
}

.graveyard ul {
	text-align: center;
	list-style-type: none;
	margin: 0;
	padding: 0;
}

.graveyard li {
	margin-bottom: 1.15em;
	text-transform: uppercase;
	letter-spacing: 10px;
}

.candle video {
	box-shadow: inset 0px 0px 50px rgba(0,0,0,1);
	position: absolute;
	bottom: 0;
	left: 0;
	right: 0;
	z-index: -1000;
}

</style>

<div class="graveyard">

<h1>RIP IN PIECES</h1>

	<ul>
	{% for person in site.data.dead %}
		<li>{{ person.name }}</li>
	{% endfor %}
	</ul>
</div>
<div class="aoe2">
	<audio src="/assets/aoe2.mp4" autoplay="autoplay" type="audio/mpeg" loop preload></audio>
</div>
<div class="candle">
	<video autoplay loop>
		<source src="/assets/candle.webm" type="video/webm">
	</video>
</div>
