# author: tfording

import numpy
import argparse
import os
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)

def parse_trinity_fasta(input_file_path):
    '''
    This function will iterate through a trinity fasta and pull lengths from header lines to pass to various functions
    :param input_file_path: Directory to file
    :return: Above parameters in a table format
    '''
    length_array = []
    fh = open(input_file_path, "r")

    for line in fh:
        if str(line[0]) == '>':
            line = line.split()
            length = line[1]
            length = length[4:]
            length_array.append(length)
    length_array_int = []

    for item in length_array:
        item = int(item)
        length_array_int.append(item)

    min = min_contig(length_array_int)
    max = max_contig(length_array_int)
    total_size = total_size_in_bp(length_array_int)
    file_name = parse_file_name(input_file_path)
    num_contigs = len(length_array_int)
    median = median_contig(length_array_int)
    average = average_contig(length_array_int)
    n_50 = N50_func(length_array_int, total_size)

    print 'File Name:', file_name
    print 'Number of Contigs:', num_contigs
    print 'Total Size:', total_size
    print 'Min Contig Size:', min
    print 'Max Contig Size:', max
    print 'Average Contig Size:', average
    print 'Median Contig Size:', median
    print 'N50:', n_50
    contig_length_dist(length_array_int, file_name)


def contig_length_dist(length_array, file_name):
    '''
    This function plots a length distribution
    :param length_array:
    :return:
    '''
    label1 = file_name+' Contig Dist'
    plt.show(sns.distplot(length_array, bins=40, kde=False, rug=True, axlabel='Contig Length', label='LOOK AT ME'))


def N50_func(length_array, total_len):
    '''
    Calculates N50 of given array
    :param length_array: array of integers
    :return: N50 of array
    '''
    new_list = sorted(length_array)
    len_count = 0
    pos_count = 0
    for i in new_list:
        len_count += i
        if len_count >= (total_len/2.0):
            return i


def average_contig(length_array):
    '''
    :param length_array: Array of integers
    :return: mean of array
    '''
    return numpy.mean(length_array)


def median_contig(length_array):
    '''
    :param length_array: array of integers
    :return: median of array
    '''
    return numpy.median(length_array)


def parse_file_name(path_to_file):
    '''
    :param path_to_file: directory (str)
    :return: Just the file name
    '''
    path_to_file= path_to_file.split('/')
    return path_to_file[-1]


def min_contig(length_array):
    '''
    :param length_array: array of integers
    :return: min of array
    '''
    min_contig = min(length_array)
    return min_contig


def max_contig(length_array):
    '''
    :param length_array: array of integers
    :return: max of array
    '''
    max_contig = max(length_array)
    return max_contig


def total_size_in_bp(length_array):
    '''
    :param length_array: array of integers
    :return: sum of integers in array
    '''
    total_size = 0
    for item in length_array:
        total_size += item
    return total_size


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic Transcript Stats")
    parser.add_argument("input_file_path", type=str, help="Enter file path", nargs='?')
    args = parser.parse_args()

    parse_trinity_fasta(args.input_file_path)
