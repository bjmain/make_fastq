D={}
# this is the pseudohap genome after filter by sequniq.
for line in open("aws_pseudohap_uniq_apr.fa"):
        #for line in open("10x_tig233502.fa"):
        i=line.strip().split()
        if line[0]==">":
                c=i[0].strip(">")
                D[c]=[]
                #if len(D)>10:
                #    break
                continue
        D[c].extend(line.strip())

# D Key = contig #
# D values = list of 60mers for each contig
contig_list = {}
for cont in D:
    seq = "".join(D[cont]) # make one contig 
    # print 600bp reads with 300bp step
    seq_list = [seq[i:i+600] for i in xrange(0, len(seq), 300)] # len(seq) allows for the last read to be less than 100bp
    count=0
    for fragment in seq_list:
        count+=1
        name = "".join([">",cont,"_",str(count)])
        print(name)
        print(fragment)
        #print "+"
        #fake_quality_cut = "J" * int(len(cut))
        #print fake_quality_cut
    
