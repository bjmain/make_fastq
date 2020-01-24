import sys

switch=0
for line in open(sys.argv[1]):
    if line[0]==">":
        print("@"+line.strip().strip(">"))
        switch=1
        continue
    if switch:
        print(line.strip())
        print("+")
        print("I"*len(line.strip()))
    
