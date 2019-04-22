#!/usr/bin/python
import sys

countTotal = 0
highTotal = 0
oldKey = None
valueKey = None

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		# Something has gone wrong. Skip this line.
		continue

	thisKey, thisCount = data
	if oldKey and oldKey != thisKey:
		if countTotal>=highTotal:
			highTotal=countTotal
			valueKey = oldKey
		countTotal=0
		oldKey=thisKey

	oldKey = thisKey
	countTotal += int(thisCount)

if oldKey != None:
	print valueKey, "\t", highTotal
