#!/usr/bin/env python
#__author__ = 'TFording'
from sys import argv

# TODO: THIS IS BROKEN CODE!!!!!!

def kmer_dist(file_path):
    KMER_SIZE = 15
    FILE_NAME = '/Users/TFording/Desktop/BGMP/bi621/problem sets/10xoutput.lane1_NoIndex_L001_R1_003.fastq'
    dict = {}  # will hold the number of occurances of each kmer #kmer: quantity of that kmer
    dict2 = {}  # iterate over dict1 and create a kmer freq dictionary

    for i in range(1, len(argv)):  # looks at the given arguments and asks for input based on them
        if argv[i] == '-k':
            KMER_SIZE = raw_input("What size k-mer would you like to create?:")
        elif argv[i] == '-f':
            FILE_NAME = raw_input("Enter the path to your file:")

    sequence_counter = -1
    counter = 0.0
    fh = open(FILE_NAME, 'r')
    KMER_SIZE = int(KMER_SIZE)

    for line in fh:  # iterates over the lines in the file
        if sequence_counter % 4 == 0:  # isolates the sequence line
            sequence_counter += 1.0
            counter += 1
            line = line.strip()
            head_line = str(line)
        elif sequence_counter % 4 == 3:

            for i in range(len(line)):  # This kmerizes the sequence and stores it in a dict
                # print line
                # print i, int(i)+KMER_SIZE
                temp_kmer = str(line[i:(int(i)+KMER_SIZE)])
                # print len(temp_kmer), temp_kmer
                if len(temp_kmer) == KMER_SIZE:
                    if temp_kmer in dict:  # increments the value for the barcode key or adds key
                        dict[temp_kmer] = (dict[temp_kmer] + 1)
                    else:
                        dict[temp_kmer] = 1
                else:
                    continue
        else:
            sequence_counter += 1

    for key, value in dict.iteritems():  # takes the previous dict and creates a freq dist.
        if value in dict2:
            dict2[value] += 1
        else:
            dict2[value] = 1

    print '# k-mer frequency    Number of k-mers'  # prints the freq dist.
    for key, value in dict2.iteritems():
        print key, '\t', value


    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Basic Transcript Stats")
        parser.add_argument("input_file_path", type=str, help="Enter file path", nargs='?')
        args = parser.parse_args()

    parse_trinity_fasta(args.input_file_path)
