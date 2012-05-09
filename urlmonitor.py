#!/usr/bin/python

import urllib2
import re

pair = {}
pair['url'] = "http://slashdot.org"
pair['pcre'] = [r"Anonymous Coward", r"Cowboy [a-zA-Z0-9]+", r"Geeknet"]

url_pairs = []
url_pairs.append(pair)

for pair in url_pairs:
    bOffending = False
    print "\n"
    url = pair['url']
    pcre = pair['pcre']
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