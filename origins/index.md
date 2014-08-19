---
layout: page
title: Origin Stories
---

Some stories on how people found and enjoy this community.

<ul class="origins">
{% for person in site.data.origins %}
	<li>
		<dl>
			<dt><a name="{{ person.username }}"></a>Username</dt>
			<dd><a href="#{{ person.username }}">{{ person.username }}</a></dd>
			<dt>Joined</dt>
			<dd>{{ person.joined }}</dd>
			<dt>Why?</dt>
			<dd>{{ person.why }}</dd>
			<dt>Do you enjoy this community?</dt>
			<dd>{{ person.enjoy }}</dd>
		</dl>
	</li>
{% endfor %}
</ul>
