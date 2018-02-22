#author=Tyler Fording

from __future__ import division


def main(path_FASTA):
    fh_in = open(path_FASTA, 'r')
    #fh_out = open(path_out, 'w')

    lengths_array = []
    current_length = 0
    counter = 0

    for line in fh_in:
        if line[0] == '>' and counter == 0:
            counter += 1
        elif line[0] == '>' and counter >= 1:
            lengths_array.append(current_length)
            current_length = 0
        else:
            current_length += len(line)

    mean = calcMean(lengths_array)
    print "Total transcripts in transcriptome:", len(lengths_array)
    print "The mean transcript length is:", mean



def calcMean(array):
    total = 0
    for item in array:
        total += int(item)
    mean = total / len(array)
    print 'Total bp in transcriptome:', total
    return mean















main('/Volumes/projects/tfording/a_inornata/transcriptome/inornataTranscriptome.fasta')