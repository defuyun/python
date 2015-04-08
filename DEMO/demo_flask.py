#!/usr/bin/python

# WSGI even though better than us writting http request header
# is still very clumsy so we have web structs like flask to 
# make life easier

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
	return '<h>Home</h>'

@app.route('/signin',methods=['GET'])
def signin_form():
	return '''<form action='/signin', method='post'>
			  <p><input name="username"></p>
			  <p><input name="password"></p>
			  <p><button type="submit">Sign in</button></p>
			  </form> '''

@app.route('/signin',methods=['POST'])
def signin():
	if request.form['username'] == 'admin' and request.form['password'] == 'password':
		return '<h3>Hello, admin!</h3>'

	return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
	app.run()
