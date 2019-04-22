#!/usr/bin/python
import sys

countRedSox =0
countCardinals = 0
oldKey = None
oldTeam=None

for line in sys.stdin:
	data = line.strip().split(",")
	if len(data) != 3:
		# Something has gone wrong. Skip this line.
		continue

	thisKey, thisFriend, thisTeam = data
	#thisKey, thisFriend = data
	#print thisKey, "\t", thisFriend, "\t", thisTeam

	if oldKey and oldKey != thisKey and thisFriend!=thisKey:
		print oldKey, "has \t fav team:", oldTeam, "\t RedSox friends:", countRedSox, "\t Cardinals friends:", countCardinals
		oldKey = thisKey
		countRedSox = 0
		countCardinals = 0
	if thisFriend==thisKey:
		oldTeam=thisTeam
		continue
	elif thisTeam=="Red Sox":
		countRedSox+=1
	elif thisTeam=="Cardinals":
		countCardinals+=1
	oldKey = thisKey

if oldKey != None:
	print oldKey, "has \t fav team:", oldTeam, "\t RedSox friends", countRedSox, "\t Cardinals friends", countCardinals
