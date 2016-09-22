#!/usr/bin/env python
# cgi = common gateway interface, a way for the server to communicate with a program

import os
import json
import cgi
import sys

form = cgi.FieldStorage()
loggedinok = False

if form.getvalue('user') == 'bob' and form.getvalue('password') == 'password':
	loggedinok = True

if 'loggedin=true' in os.environ["HTTP_COOKIE"]:
	loggedinok=True

print "Content-Type: text/html"
if loggedinok:
	print "Set-Cookie: loggedin=true"
print
# have to put print lne or else te next line is assumed to till be header
print "<HTML><BODY><H1> Hello, World! </H1>"
print "<FORM method = 'POST'><INPUT name = 'user' />"
print "  <INPUT name = 'password' type = 'password'>"
print "  <BUTTON type = 'submit'> Log In </BUTTON>"
print "  </FORM>"

if loggedinok:
	print " LOG IN OK!"
# have to put ?q=x after html adress t give query string
#print "<P> Query string was: " + os.environ["QUERY_STRING"] + "</P>"
##print "<P> Your browser is: " + os.environ["HTTP_USER_AGENT"] + "</P>"
#print "<P>"
  # module for reading standard input instead of just getting a bunch of % for special characters
#print "Username was: " + form.getvalue("user") + "."
#print "Password was: " + form.getvalue("password") + "." 
#print "</P>"

cgi.print_environ()

print json.dumps(dict(os.environ), indent = 4)

print "</BODY></HTML>"
