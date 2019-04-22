#!/usr/bin/python
import sys

#read data input line by line
for line in sys.stdin:
	data = line.strip().split("\t")
	
	if len(data)!=6:
		continue

	date, time, store, item, cost, payment = data

	#print out data
	print "{0}\t{1}".format(store,cost)
	#print "{0}\t{1}".format(item,cost)
