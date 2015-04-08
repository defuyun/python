#!/usr/bin/python

from HTMLParser import HTMLParser
import urllib2
import re

url = 'https://www.python.org/events/python-events/'

class collector(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.comment = []
		self.data = []

	def handle_starttag(self,tag,attr):
		if tag == 'time' and 
	def handle_comment(self,data):
		self.comment.append(data.strip())

	def handle_data(self,data):
		if not re.match(r'^\s*$',data):
			self.data.append(dat.strip())


content = urllib2.urlopen(url).read()
parser = collector()
parser.feed(content)
parser.close()

for data in parser.data:
	print data