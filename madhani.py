##This script will make madhani data intelligible

##first, read in data

def readArrayFile(arrayFile):
	probeHash = {}
	for line in arrayFile:
		listline = line.rstrip().split('\t')
		try:
			probeID = int(listline[0])
		except ValueError:
			print "testing"