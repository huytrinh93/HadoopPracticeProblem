#!/usr/bin/python
import sys

salesCount =0
salesTotal = 0
oldKey = None

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		# Something has gone wrong. Skip this line.
		continue

	thisKey, thisSale = data
	
	#convert to int
	try:
		thisSale = float(thisSale)
	except ValueError:
		#not a number
		#discard this line
		continue

#	if oldKey and oldKey != thisKey:
#		print oldKey, "\t", salesCount, "\t", salesTotal
#		oldKey = thisKey
#		salesCount = 0
#		salesTotal = 0

#	oldKey = thisKey
	salesTotal+= (thisSale)
	salesCount+= 1

#if oldKey != None:
print "all \t", salesCount, "\t",salesTotal
