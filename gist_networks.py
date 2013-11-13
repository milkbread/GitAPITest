#!/usr/bin/python

import pycurl
import cStringIO


def simpleRequest(url):
    buf = cStringIO.StringIO()
 
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.HTTPHEADER, [
    	'Authorization:milkbread'
    ])
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.perform()
    print c.getinfo(pycurl.HTTP_CODE), c.getinfo(pycurl.EFFECTIVE_URL)
     
    response = buf.getvalue()
    buf.close()
    return response

curl = pycurl.Curl()
#print dir(curl)
user = 'milkbread'

req = simpleRequest("https://api.github.com/users/" + user + "/gists")
print req