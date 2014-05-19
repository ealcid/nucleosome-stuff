import sys

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

pughFile = open(sys.argv[1], 'r')

pughFile.readline() #get rid of header

of = open("isw2_nucleosomes.sgr", 'w')

for line in pughFile:
	listline = line.rstrip().split('\t')
	total = float(listline[2])+float(listline[3])
	of.write("%s\t%s\t%s\n" % (chromDict[listline[0]], listline[1], total))