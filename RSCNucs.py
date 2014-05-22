##This script will make madhani data into sgr format <chrom> <position> <value>

##first, read in data

import sys
def changeChromes(chrom):
	##sometimes input files names chromosomes differently, returns roman numeral chromosome names
	chromDict = {"chr01":"I",
				"chr02":"II",
				"chr03":"III", 
				"chr04":"IV",
				"chr05":"V",
				"chr06":"VI",
				"chr07":"VII",
				"chr08":"VIII",
				"chr09":"IX",
				"chr10":"X",
				"chr11":"XI",
				"chr12":"XII",
				"chr13":"XIII",
				"chr14":"XIV",
				"chr15":"XV",
				"chr16":"XVI",
				"1":"I",
				"2":"II",
				"3":"III", 
				"4":"IV",
				"5":"V",
				"6":"VI",
				"7":"VII",
				"8":"VIII",
				"9":"IX",
				"10":"X",
				"11":"XI",
				"12":"XII",
				"13":"XIII",
				"14":"XIV",
				"15":"XV",
				"16":"XVI"}
	return chromDict[chrom]

def readArrayFile(arrayFile):
	probeHash = {}
	for line in arrayFile:
		listline = line.rstrip().split('\t')
		try:
			probeID = int(listline[0])
			float(listline[1])
			#probeHash[probeID] = float(listline[1])
		except ValueError:
			#print "not a number", line
			pass
		except:
			#print "value is missing", listline
			probeHash[probeID] = "missing"
			pass
		else:
			probeHash[probeID] = float(listline[1])
	arrayFile.close()
	return probeHash

def getKey(item):
	return item[[-1]]

def smoothing(item): #5 probe smoothing
	sum = 0
	for i in range(len(item)):
		sum += float(item[i])
	average = sum/len(item)
	return average
		

def main():
	rep1 = open(sys.argv[1])
	probeHash1 = readArrayFile(rep1)
	rep2 = open(sys.argv[2])
	probeHash2 = readArrayFile(rep2)
	rep3 = open(sys.argv[3])
	probeHash3 = readArrayFile(rep3)
	rep4 = open(sys.argv[4])
	probeHash4 = readArrayFile(rep4)
	mergedHash = {}
	for key in probeHash1.keys():
		totalList = [probeHash1[key], probeHash2[key], probeHash3[key], probeHash4[key]]
		for x in totalList:
			sum = 0
			divisor = 0
			if x == 'missing': continue
			else:
				sum += x
				divisor += 1
			average = sum/divisor
			mergedHash[key] = average
	##mergedHash: key->probeID, hash->log2Value
	##now need to take the platform, and translate it into chromosome and position
	##now open platform, and convert it to something that makes sense, like chrom <tab> position <tab> value
	platform = open("platform.txt")
	coordHash = {}
	for i in range(4):
		platform.readline() ##get rid of header

	for line in platform:
		listline = line.rstrip().split('\t')
		coordinates = listline[-1].split('[')[-1].replace(']', '').split('..')
		start = int(coordinates[0])
		end = int(coordinates[1])
		midpoint = start + ((start-end)/2)
		if changeChromes(listline[1]) not in coordHash:
			coordHash[changeChromes(listline[1])] = [[int(listline[0]), changeChromes(listline[1]), midpoint]]
		else:
			coordHash[changeChromes(listline[1])].append([int(listline[0]), changeChromes(listline[1]), midpoint])

	for key in coordHash:
		coordHash[key].sort(key = lambda feature:feature[-1])

	#print coordHash
	#perform smoothing
	for key in coordHash.keys():
		for i in range(len(coordHash[key])):
			if i < 2 or i >= len(coordHash[key])-2: continue
			else:
				tempArray = []
				for j in range(i-2, i+3): 
					if coordHash[key][j][0] not in mergedHash: continue
					else:
						tempArray.append(mergedHash[coordHash[key][j][0]])
				if len(tempArray) == 0:
					coordHash[key][i].append(0)
					continue
				else:
					print smoothing(tempArray)
					coordHash[key][i].append(smoothing(tempArray))
	
	print coordHash

	output = open("sth1DegOn.sgr", 'w')
	smoothed = open("sth1DefOnSmooth.sgr", 'w')
	for key in coordHash.keys():
		for item in coordHash[key]:
			#print "%s\t%s\t%s\n" % (key, item[-1], mergedHash[item[0]])
			if item[0] not in mergedHash: continue
			else:
				output.write("%s\t%s\t%s\n" % (key, item[2], mergedHash[item[0]]))
				smoothed.write("%s\t%s\t%s\n" % (key, item[2], item[-1]))
	



if __name__ == '__main__':
	main()