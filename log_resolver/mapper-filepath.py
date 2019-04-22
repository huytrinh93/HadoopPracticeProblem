#!/usr/bin/python
import sys
import re
from urlparse import urlparse

#read data input line by line
for line in sys.stdin:
	line = line.strip()
	firstIndex = line.find("\"")
	lastIndex = line.rfind("\"")
	#print "{0}\t{1}".format(firstIndex,lastIndex)
	#print out data
	if(firstIndex>1 and lastIndex>2):
		requestString = line[firstIndex+1:lastIndex]
		#print(requestString)
		actualUrl = requestString.split(" ")[1]
		#print actualUrl
		filepath = urlparse(actualUrl)
		#print filepath
		#print filepath.path
		print "{0}\t{1}".format(filepath.path,1)
