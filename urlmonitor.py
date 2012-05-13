#!/usr/bin/python
#
#   urlmonitor
#
#   license: gnu gpl v3
#   author: will urbanski
#

import urllib2
import re
import json
import hashlib
import time

from pprint import pprint
from urlparse import urlparse
from optparse import OptionParser

#the default path for the signature file
file_path = "urls.json"

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="read signatures from FILE", metavar="FILE")
(options, args) = parser.parse_args()
if (options.filename != None):
    file_path = options.filename

#load urls.json for monitoring
json_data=open(file_path).read()
data = json.loads(json_data)

domains = []
urls = 0
checks = 0
matches = 0

for item in data:
    url = item['url']
    pcre = item['pcre']
    
    oURL = urlparse(url)
    domains.append(oURL.netloc)
    urls += 1
    
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    md5sum = hashlib.md5()
    md5sum.update(the_page)
    for s_pcre in pcre:
        m = re.search(s_pcre,the_page)
        checks += 1
        if (m != None):
            print "%s,\"%s\",\"%s\",\"%s\",\"%s\",\"%s\"" % (time.time(),oURL.netloc,url,md5sum.hexdigest(),s_pcre,m.group(0))
            matches += 1