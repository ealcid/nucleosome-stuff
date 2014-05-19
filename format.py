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

def changePugh(file,output, head=True):
	##combines forward and reverse reads into a total and outputs file
	if head==True: header = file.readline() #get rid of header
	assert len(header.split()) == 4 ##make sure the input is a pugh genetrack file 
	for line in file:
		listline = line.rstrip().split('\t')
		total = float(listline[2])+float(listline[3])
		output.write("%s\t%s\t%s\n" % (changeChromes(listline[0]), listline[1], total))

def main():
	pughFile = open(sys.argv[1])
	output = open(sys.argv[2], 'w')
	changePugh(pughFile, output, head=True)

if __name__ == '__main__':
	main()