#!/usr/bin/python
import sys

salesHigh = 0
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

	if oldKey and oldKey != thisKey:
		print oldKey, "\t", salesHigh
		oldKey = thisKey
		salesHigh = 0

	oldKey = thisKey
	if thisSale>=salesHigh:
		salesHigh = thisSale

if oldKey != None:
	print oldKey, "\t", salesHigh
