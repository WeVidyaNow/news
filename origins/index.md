---
layout: page
title: Origin Stories
---

<ul class="origins">
{% for person in site.data.origins %}
	<li>
		<dl>
			<dt>Username</dt>
			<dd>{{ person.username }}</dd>
			<dt>Joined</dt>
			<dd>{{ person.joined }}</dd>
			<dt>Why?</dt>
			<dd>{{ person.why }}</dd>
			{% if person.enjoy %}
				<dt>Do you enjoy this community?</dt>
				<dd>{{ person.enjoy }}</dd>
			{% endif %}
		</dl>
	</li>
{% endfor %}
</ul>
