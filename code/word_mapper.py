#!/usr/bin/python
import sys

#read data input line by line
for line in sys.stdin:
	data = line.strip()
	
	if len(data)!=6:
		continue
	#alphabet sort
	result = sorted(data)
	#print out data
	print "{0}\t{1}".format(''.join(result),data)
	#print "{0}\t{1}".format(item,cost)
