import sys
import os
import getopt
import re
import requests

inputfile = ''
outputfile = ''
try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
except getopt.GetoptError:
    print("sort.py -i <inputfile> -o <outputfile>")
    sys.exit(2)

for opt,arg in opts:
    if opt == '-h':
        print("sort.py -i <inputfile> -o <outputfile>")
        sys.exit()
    elif opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-o", "--ofile"):
        outputfile = arg

print("input file is : " + inputfile + ", output file is " + outputfile)

# remove brackets from file
ifile = ''
with open(inputfile, "r") as f:
    ifile = str(f.read())

ifile_no_bracket = ifile.replace("[", "")
ifile_no_bracket = ifile_no_bracket.replace("]", "")

#extract all url
pattern = re.compile(r'"*(.*?)\s*"')
count = 0
with open(outputfile, "a") as f2:
    for match in re.findall(pattern, ifile_no_bracket):
        if match != ",":
            count += 1
            f2.write(match+"\n")
print("number of urls : " + str(count))

f.close()
f2.close()
