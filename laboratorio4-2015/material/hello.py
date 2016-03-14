#!/usr/bin/python

from datetime import datetime

print 'Content-Type: text/html'
print
print '<html>'
print '<head><title>Hello from Python</title></head>'
print '<body>'
print '<h2>Hello from Python</h2>'
print '<h3>'
print str(datetime.now())
print '</h3>'
print '</body></html>'
