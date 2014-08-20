---
layout: page
title: Graveyard
---

<div class="graveyard">
	<ul>
	{% for person in site.data.dead %}
		<li>{{ person.name }}</li>
	{% endfor %}
	</ul>
</div>
