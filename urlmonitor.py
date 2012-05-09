#!/usr/bin/python

import urllib2
import re
import json
from pprint import pprint

#load urls.json for monitoring
json_data=open("urls.json").read()
data = json.loads(json_data)

for item in data:
    bOffending = False
    print "\n"
    url = item['url']
    pcre = item['pcre']
    print "Checking %s" % url
    
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    for s_pcre in pcre:
        m = re.search(s_pcre,the_page)
        if (m != None):
            print "Match found: %s" % m.group(0)
            bOffending = True
        else:
            print "Match not found: %s" % s_pcre
    if (bOffending == True):
        print " ++ URL is offending! ++"
    else:
        print " -- URL is clean --"
    
    #print the_page