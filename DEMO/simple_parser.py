#!/usr/bin/python

from HTMLParser import HTMLParser

html = '''<time datetime="2015-02-06T00:00:00+00:00">06 Feb. &ndash; 09 Feb. <span class="say-no-more"> 2015</span></time>

                            

                            
                            <span class="event-location">Nashville, TN</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/248/">Building Better Python Tools Hackathon</a></h3>
'''
class collector(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.time = []
		self.location = []
		self.event = []

		self.timeflag = False
		self.locationflag = False
		self.eventflag = False

	def handle_starttag(self,tag,attr):
		if tag == 'time':
			self.timeflag = True
		
		if tag == 'span' and len(attr) == 2 and attr[1] == 'event-location':
			self.locationflag = True
		
		if tag == 'h3' and len(attr) == 2 and attr[1] == 'even-title':
			self.eventflag = True

	def handle_endtag(self,tag):
		if tag == 'time':
			self.timeflag = False

	def handle_data(self,data):
		if self.timeflag:
			self.time.append(data.strip())

		if self.locationflag:
			self.location.append(data.strip())
		
		if self.eventflag:
			self.event.append(data.strip())

parser = collector()
parser.feed(html)
parser.close

print parser.time
print parser.location
print parser.event