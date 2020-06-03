import sys

read_len = 100
step_size = 100

D={}
# input fasta file after the python script: python make_fastq.py species.fa
for line in open(sys.argv[1]):
        i=line.strip().split()
        if line[0]==">":
                c=i[0].strip(">")
                D[c]=[]
                continue
        D[c].extend(line.strip())



contig_list = {}
for cont in D:
    seq = "".join(D[cont]) # make one contig 
    seq_list = [seq[i:i+read_len] for i in xrange(0, len(seq), step_size)] # len(seq) allows for the last read to be less than 100bp
    count=0
    for fragment in seq_list:
        count+=1
        name = "".join([">",cont,"_",str(count)])
        print(name)
        print(fragment)
        print "+"
        fake_quality = "J" * int(len(fragment))
        print fake_quality   # Be careful with this!
