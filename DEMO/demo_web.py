#!/usr/bin/python

# in the old times, apps are run on large machines and people acces them through
# servers. recently, apps started running on PCs and access information through the
# database stored on the server, this mode is called CS (Clent/Server)

# after a while when internet started booming, the cs mode seems antiquated becuase
# web apps advanced rapidaly and this means that the home app must also be upgraded from
# tiem to time

# then there came the BS mode Browser/Server where the browser stores all information
# and reacts to the server

# a simple web app stores a html page somewhere, and opens an HTTP server
# when some server requires it, return the html, examples of these http servers
# includes Apache, nginx, Lighttpd

# WSGI is a lower interface used to produce a HTTP server
# it's responsible for analysing http request and doing all the
# lower jobs such as connections etc

# when we use the WSGI, we create an application that receives the environment and 
# a response functio, the reponse function will produce the header (this is created 
# by the WSGI) and we can use data in env to produce our html

# so make it simple, WSGI will create a header for us so we don't have to worry about
# the lower stuff

# threre are tons of WSGI interface out there and python has a built-in one called
# wsgiref

from wsgiref.simple_server import make_server

def dict2string(env):
	return '\n'.join([str(key).strip() + ':' + ''.join(str(val).strip()) for key,val in env.iteritems()])

def application(env,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	return '<pre>%s</pre>' % dict2string(env)

httpd = make_server('',8000,application)
print 'Serving on port 8000....'

httpd.serve_forever()

