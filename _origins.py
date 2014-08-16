#!/usr/bin/env python
import csv, sys, datetime

responses = []
with open(sys.argv[1], 'rb') as f:
	reader = csv.reader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
	for row in reader:
		responses.append(
			{
			'name': row[1].replace('\n', ''),
			'joined': row[2].replace('\n', ''),
			'why': row[3].replace('\n', ''),
			'enjoyed': row[4].replace('\n', ''),
			'publish': row[5].replace('\n', '')
			}
		)

print "\nTotal of {0} responses.\n".format(str(len(responses)))
for person in responses:
	print """username: {0}
joined: {1}
why: {2}
enjoyed: {3}
publish: {4}
""".format(person['name'], person['joined'], person['why'], person['enjoyed'], person['publish'])

with open(sys.argv[2], 'a') as f:
	for person in responses:
		datestr = person['joined'].split('/')
		joined = datetime.date(int(datestr[2]), int(datestr[0]), 1)
		joinstr = joined.strftime("%b %Y")
		if person['publish'].lower() == 'yes':
			f.write("""
- username: {0}
  joined: {1}
  why: {2}
  enjoy: {3}""".format(person['name'], joinstr, person['why'], person['enjoyed']))
		else:
			f.write("""
- username: {0}
  joined: {1}
  why: {2}""".format(person['name'], joinstr, person['why']))
