---
layout: post
author: Battleroid
title: "Our Own Twitch? Part 2"
categories: update
date: 2014-08-08
---

After doing some testing on a local VM, it's pretty fucking cool and easy to setup. Not to mention streaming (without any transcoding) is really lightweight on the server. Streaming at 3500Kb/s literally had no impact on the VM at all.

Definitely doable, only problem is making a frontpage for active streams. The only way I can see to do it at the current time is parsing the statistics put out from the RTMP module (in XML format). Which is fine, but that means it'd have to parse the junk every time you open the frontpage up.

I'd like to have a MySQL database running for it, but I have to figure out how on\_publish\_done works.
