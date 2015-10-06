__author__ = 'Jonathan Rubin'

##contains a list of helpful functions

import os
import sys
#sys.path.append("C:\home\Jonathan\interval_searcher")
from operator import itemgetter
import node

#Create a dictionary from a bed file with chromosome locations creates a list of lists [start,stop] for each chrom
#(format needs to be: 'Chromosome'\t'Start'\t'Stop'..., if header = True, remove first line of file containing header info)
def create_dict(filename, header):
    d1 = dict()
    file1 = open(filename)
    if header:
        file1.readline()
    for line in file1:
        chrom, start, stop = line.strip().split()[0:3]
        if chrom in d1:
            d1[chrom].append([float(start),float(stop)])
        else:
            d1[chrom] = [[float(start), float(stop)]]
    return d1
    
#Create a dictionary from a bed file with chromosome locations creates list of tuples (start,stop) for each chrom
#(format needs to be: 'Chromosome'\t'Start'\t'Stop'..., if header = True, remove first line of file containing header info)
def create_tup_dict(filename, header):
    d1 = dict()
    file1 = open(filename)
    if header:
        file1.readline()
    for line in file1:
        chrom, start, stop = line.strip().split()[0:3]
        if chrom in d1:
            d1[chrom].append((float(start),float(stop)))
        else:
            d1[chrom] = [(float(start), float(stop))]
    return d1
    
#Create a dictionary from a bed file with chromosome locations creates list of tuples (start,stop) for each chrom
#(format needs to be: 'Chromosome'\t'Start'\t'Stop'..., if header = True, remove first line of file containing header info)
def create_tup_dict_largeheader_strandprob(filename, headerlines):
    d1 = dict()
    file1 = open(filename)
    for i in range(0,headerlines):
        file1.readline()
    for line in file1:
        chrom, start, stop = line.strip().split()[0:3]
        if chrom in d1:
            d1[chrom].append((float(start),float(stop),line.strip().split()[3].split('_')[4]))
        else:
            d1[chrom] = [(float(start), float(stop),line.strip().split()[3].split('_')[4])]
    return d1
    
#Returns a list of arrays for a file with each item in list a line and each array contains tab delimited fields (i.e. list = [[chrom, start, stop],[chrom,start,stop], ...etc.]) 
def parse_file(filename):
    FileList = []
    for line in open(filename):
        FileList.append(line.strip().split('\t'))
    
    return FileList
    
#Writes an outfile based on a list of arrays 
def write_file(inlist, outfilename):
    outfile = open(outfilename, 'w')
    for item in inlist:
        for field in item:
            outfile.write(field)
            outfile.write("\t")
        outfile.write("\n")

#Returns outfile with columns specified of infile. Requires a list of columns
def cut_file(infilename, columns, outfilename):
    outfile = open(outfilename, 'w')
    FileList = parse_file(infilename)
    for item in FileList:
        for column in columns:
            outfile.write(item[column])
            outfile.write("\t")
        outfile.write("\n")
    

#Order a tab delimited file by chromosome then start position (if header = True then save first line as header):
def order_file(filename, outfilename, header):
    file1 = open(filename)
    if header:
        header1 = file1.readline()
    d2 = dict()
    for line in file1:
        chrom, start = line.strip().split()[0:2]
        if chrom in d2:
            d2[chrom].append((float(start),line))
        else:
            d2[chrom] = [(float(start), line)]
    
    outfile2 = open(outfilename, 'w')
    if header:
        outfile2.write(header1)
    for chrom in d2:
        linelist = sorted(d2[chrom],key=itemgetter(0))
        for line in linelist:
            outfile2.write(line[1])

    
#Removes duplicate intervals from a file. Needs infilename and outfilename. If header = True then will not evaluate first line and will rewrtie first line in outfile
def remove_duplicates_int(infilename, outfilename, header):
    d1 = dict()
    file1 = open(infilename)
    if header:
        header = file1.readline()
    for line in file1:
        chrom,start,stop = line.strip().split()[0:3]
        d1[chrom + ": " + start + "-" + stop] = line
    outfile = open(outfilename, 'w')
    if header:
        outfile.write(header)
    for key in d1:
        outfile.write(d1[key])
        

#Replaces header of a file with specified header
def replace_header(filename, header):
    FileList = parse_file(filename)
    outfile = open(filename, 'w')
    outfile.write(header)
    outfile.write("\n")
    for i in range(1,len(FileList)):
        for item in FileList[i]:
            outfile.write(item)
            outfile.write("\t")
        outfile.write("\n")
        
#Removes lines x to y of a file
def remove_lines(file1, x, y):
    file1list = parse_file(file1)
    for i in range(x,y):
        file1list.pop([i])
    write_file(file1list,file1)
        
        
    
#Get line count from a file
def line_count(filename):
    i = 0
    for line in open(filename):
        i+=1
    return i
    
    
#Return a list of peak_file directories
def chip_peak_directories(rootdirectory):
    directorylist = []
    for TF in os.listdir(rootdirectory):
        directorylist.append(rootdirectory + "/" + TF + "/peak_files")
    return directorylist


#Return a list of fimo_out directories
def fimo_directories(rootdirectory):
    directorylist = []
    for TF in os.listdir(rootdirectory):
        if os.path.exists(rootdirectory + "/" + TF + "/peak_files/outfiles/MEME"):
            os.chdir(rootdirectory + "/" + TF + "/peak_files/outfiles/MEME")
            FileList = [item for item in os.listdir(os.getcwd()) if 'fimo_out' in item]
            for fimofolder in FileList:
                directorylist.append(rootdirectory + "/" + TF + "/peak_files/outfiles/MEME/" + fimofolder)
    
    return directorylist
        
#Return parent directory
def parent_dir(directory):
    pathlist = directory.split('/')
    newdir = '/'.join(pathlist[0:len(pathlist)-1])
    
    return newdir
    
#returns filename for desired modification by finding index('.') and returning substring[0:lastindex('.')] + mod + substring[lastindex('.'):endofstring]
def get_mod_filename(filename, mod):
    
    return filename[0:filename.rfind('.')] + '.' + mod + filename[filename.rfind('.'):len(filename)]

#Return list of intersecting tuples
def overlapping_list(tree, list1):
    list2 = []
    d1 = dict()
    for item in list1:
        for tup in tree.searchInterval(item):
            d1[tup] = []
    for key in d1:
        list2.append(key)
    
    return list2
    

#Returns categories for a 3-way venn diagram, requires BED files with column structure (chrom\tstart\tstop)
def venn_d3(A, headerA, B, headerB, C, headerC):
    Aparse = parse_file(A)
    Adict = dict()
    Bparse = parse_file(B)
    Bdict = dict()
    Cparse = parse_file(C)
    Cdict = dict()
    Atot = line_count(A)
    Btot = line_count(B)
    Ctot = line_count(C)
    AB = 0
    BA = 0
    AC = 0
    CA = 0
    BC = 0
    CB = 0
    ABC = 0
    CAB = 0
    BAC = 0
    if headerA == True:
        for item1 in Aparse[1:len(Aparse)]:
            chrom,start,stop = item1[0:3]
            start = int(start)
            stop = int(stop)
            if chrom not in Adict:
                Adict[chrom] = [(start,stop)]
            else:
                Adict[chrom].append((start,stop))
    else: 
        for item1 in Aparse:
            chrom,start,stop = item1[0:3]
            start = int(start)
            stop = int(stop)
            if chrom not in Adict:
                Adict[chrom] = [(start,stop)]
            else:
                Adict[chrom].append((start,stop))
    
    if headerB == True:
        for item2 in Bparse[1:len(Bparse)]:
            chrom,start,stop = item2[0:3]
            start = int(start)
            stop = int(stop)
            if chrom not in Bdict:
                Bdict[chrom] = [(start,stop)]
            else:
                Bdict[chrom].append((start,stop))
    else:
        for item2 in Bparse:
            chrom,start,stop = item2[0:3]
            start = int(start)
            stop = int(stop)
            if chrom not in Bdict:
                Bdict[chrom] = [(start,stop)]
            else:
                Bdict[chrom].append((start,stop))
                
    if headerC == True:
        for item3 in Cparse[1:len(Cparse)]:
            chrom,start,stop = item3[0:3]
            start = int(start)
            stop = int(stop)
            if chrom not in Cdict:
                Cdict[chrom] = [(start,stop)]
            else:
                Cdict[chrom].append((start,stop))
    else:
        for item3 in Cparse:
            chrom,start,stop = item3[0:3]
            start = int(start)
            stop = int(stop)
            if chrom not in Cdict:
                Cdict[chrom] = [(start,stop)]
            else:
                Cdict[chrom].append((start,stop))
    
    for chrom in Adict:
        if chrom in Bdict and chrom in Cdict:
            Alist = Adict[chrom]
            Blist = Bdict[chrom]
            Clist = Cdict[chrom]
            Atree = node.tree(Alist)
            Btree = node.tree(Blist)
            Ctree = node.tree(Clist)
            
            ABint = overlapping_list(Atree, Blist)
            BAint = overlapping_list(Btree, Alist)
            ACint = overlapping_list(Atree, Clist)
            CAint = overlapping_list(Ctree, Alist)
            BCint = overlapping_list(Btree, Clist)
            CBint = overlapping_list(Ctree, Blist)
            
            if len(ABint) == 0:
                ABCint = []
            else:
                ABtree = node.tree(ABint)
                ABCint = overlapping_list(ABtree, Clist)
            
            if len(BAint) == 0:
                BACint = []
            else: 
                BAtree = node.tree(BAint)
                BACint = overlapping_list(BAtree, Clist)
            
            if len(CAint) == 0:
                CABint = []
            else:
                CAtree = node.tree(CAint)
                CABint = overlapping_list(CAtree, Blist)
            
            AB += len(ABint)
            BA += len(BAint)
            AC += len(ACint)
            CA += len(CAint)
            BC += len(BCint)
            CB += len(CBint)
            ABC += len(ABCint)
            CAB += len(CABint)
            BAC += len(BACint)
    AB = AB - ABC
    AC = AC - ABC
    Atot = Atot - AB - AC - ABC
    BA = BA - BAC
    BC = BC - BAC
    Btot = Btot - BA - BC - BAC
    CA = CA - CAB
    CB = CB - CAB
    Ctot = Ctot - CA - CB - CAB
    
    return [Atot, Btot, Ctot, AB, BA, AC, CA, BC, CB, ABC, CAB, BAC]
    

#For each site in file1, get middle point and add and subtract pad.  For each site in file2, 
#determine whether site is in file1, if so get distance from middle of site in file2 to middle 
#of site in file1. Returns list of distances.
def get_distances_pad(file1, header1, file2, header2, pad):
    file1dict = create_tup_dict(file1, header1)
    file2dict = create_tup_dict(file2, header2)
    distances = []
    for chrom in file1dict:
        if chrom in file2dict:
            file1list = file1dict[chrom]
            chromtree = []
            for item1 in file1list:
                start, stop = item1[0:2]
                mid = (float(start)+float(stop))/2
                chromtree.append((mid-pad,mid+pad))
            chromtree = node.tree(chromtree)
            for item2 in file2dict[chrom]:
                for item3 in chromtree.searchInterval(item2):
                    start1 = float(item3[0])
                    stop1 = float(item3[1])
                    i = (start1+stop1)/2
                    start2 = float(item2[0])
                    stop2 = float(item2[1])
                    x = (start2+stop2)/2
                    distances.append((i-x)/((stop1-start1)/2))
                    
    return distances
    
#For each site in file1, get middle point and add and subtract pad.  For each site in file2, 
#determine whether site is in file1, if so get distance from middle of site in file2 to middle 
#of site in file1. Returns list of distances.
def get_distances_pad_directional(file1, headerlines, file2, header2, pad):
    file1dict = create_tup_dict_largeheader_strandprob(file1, headerlines)
    file2dict = create_tup_dict(file2, header2)
    distances = []
    for chrom in file1dict:
        if chrom in file2dict:
            file1list = file1dict[chrom]
            chromtree = []
            for item1 in file1list:
                start, stop, pi = item1[0:3]
                mid = (float(start)+float(stop))/2
                chromtree.append((mid-pad,mid+pad,pi))
            chromtree = node.tree(chromtree)
            for item2 in file2dict[chrom]:
                for item3 in chromtree.searchInterval(item2):
                    start1 = float(item3[0])
                    stop1 = float(item3[1])
                    pi = float(item3[2])
                    i = (start1+stop1)/2
                    start2 = float(item2[0])
                    stop2 = float(item2[1])
                    x = (start2+stop2)/2
                    if pi > 0.5:
                        distances.append(-(i-x)/((stop1-start1)/2))
                    else:
                        distances.append((i-x)/((stop1-start1)/2))
                    
    return distances
                
            