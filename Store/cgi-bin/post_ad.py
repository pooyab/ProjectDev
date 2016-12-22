#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

print "Content-type: text/html\n\n"


form = cgi.FieldStorage()
year = form.getvalue("year")

if "year" not in form:
    print "The text area was empty."
else:
    text=form["year"].value
    print "<h1>Year of car:</h1>"
    print cgi.escape(text)