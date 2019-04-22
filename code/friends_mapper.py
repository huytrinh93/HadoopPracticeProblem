#!/usr/bin/python
import sys

#read data input line by line
for line in sys.stdin:
	data = line.strip().split(",")
	
	if len(data)<3:
		continue
	print "{0},{1},{2}".format(data[0].strip(),data[0].strip(),data[1].strip())
	for n in range(2,len(data)):
		#if data[0]=="Alivia":
		print "{0},{1},{2}".format(data[n].strip(),data[0].strip(),data[1].strip())
		#print "{0},{1}".format(data[n],data[0])
