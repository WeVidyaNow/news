---
layout: page
---

<script type="text/javascript" charset="utf-8" src="js/jquery.tubular.1.0.js"></script>
<script type="text/javascript" charset="utf-8" src="js/index.js"></script>

<style type="text/css">
@-webkit-keyframes usa {
	0% {color: red;}
	25% {color: white;}
	50% {color: blue;}
	75% {color: white;}
	100% {color: red;}
}
body { background: none !important; margin: 0; }
header > h1 { margin-top: 0; padding-top: 15px; }
.wrapper { margin-top: 0; padding-top: 8px; color: white !important; }
article { font-family: "Times New Roman", Times, serif !important; font-size: 2em; line-height: 2em; text-align: center; text-shadow: 0px 1px 5px rgba(0, 0, 0, 1), 0px 1px 5px rgba(0, 0, 0, 1); -webkit-animation-direction: normal; -webkit-animation-duration: 10s; -webkit-animation-iteration-count: infinite; -webkit-animation-name: usa; -webkit-animation-timing-function: ease; }
article ul { list-style: none; padding: 0; }
</style>

<h1>TRUE 'MURRICANS</h1>

<ul>
	{% for person in site.data.usa %}
	<li>{{ person.name }}</li>
	{% endfor %}
</ul>

<audio src="fuckyeah.m4a" autoplay="autoplay" type="audio/mp4" loop preload></audio>
