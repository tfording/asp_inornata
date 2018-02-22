import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os
import argparse
import math


def histogram(file_path):
    '''
    This function takes a jellyfish.kmers.fa.histo file from Trinity and plots a histogram.
    :param file_path: Path to jellyfish.kmers.fa.histo
    :return: Nothing is returned, a histogram is plotted
    '''
    fh = open(file_path, "r")
    kmer_freq = []
    num_kmers = []

    for line in fh:
        line = line.split()
        kmer_freq.append(int(line[0]))
        num_kmers.append(math.log10(int(line[1])))
    #print kmer_freq, num_kmers
    # the histogram of the data

    fig = plt.figure()
    ax = fig.add_subplot(111)

    fig_size = plt.rcParams["figure.figsize"]

    fig.set_size_inches(10,12)

    ax.bar(kmer_freq, num_kmers, width=100, color='b', edgecolor='b')

    ax.set_xlabel('Freq of Kmer')
    ax.set_ylabel('Num of Kmer (Log10)')
    ax.set_title('Kmer Dist')

    ax.grid(True)

    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic Transcript Stats")
    parser.add_argument("input_file_path", type=str, help="Enter file path", nargs='?')
    args = parser.parse_args()

histogram(args.input_file_path)