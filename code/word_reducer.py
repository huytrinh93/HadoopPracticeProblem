#!/usr/bin/python
import sys

count = 0 
oldKey = None
oldWord = None
previousKey = None
previousWord = None

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		# Something has gone wrong. Skip this line.
		continue

	thisKey, thisWord = data

	if oldKey and oldKey != thisKey:
	#	if count=2:
	#		print oldKey, "\t", oldWord, "\t", count
		count=0
	#	oldKey = thisKey
	#	oldWord = thisWord
	else:
		count+=1
		if count==2:
			print oldKey, "\t", oldWord, "\t", count
		if count>=2:
			print thisKey,"\t",thisWord,"\t",count
	oldKey=thisKey
	oldWord=thisWord


if oldKey != None:
	if count>=2:
		print oldKey, "\t", oldWord, "\t", count
