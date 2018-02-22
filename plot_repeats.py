#author=Tyler Fording

from __future__ import division
import argparse
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


def plot_repeats(file_path1):
    fh_in = open(file_path1, 'r')
    line_list = []


    ############################################  Read in file
    for line in fh_in:
        line = line.strip('\n')
        line = line.split()
        for i in line:
            i = i.strip
        if float(line[3]) > 0.0010:
            line_list.append(line)

    ############################################  Populate data structures for plotting
    x_tick_labels = [i[0].strip() for i in line_list]

    x_list = [i+1 for i in range(len(line_list))]

    y_list = [float(i[3].strip()) for i in line_list]

    data = []
    new_line_list = []

    for item in line_list:
        data.append({'label':item[0], 'color':'maroon', 'height':float(item[3])})


    ############################################  Plot data
    figure, ax = plt.subplots()
    i = 1
    for bar in data:
        ax.bar(i, bar['height'], align='center', color=bar['color'])
        i += 1

    plt.xticks(x_list, x_tick_labels, rotation=45, ha='right')
    plt.ylabel('% Abundence')
    plt.xlabel('Repeat Class')
    plt.title('Gularis Repeat Abundence by Class')

    for i in x_list:
        ax.text(i, y_list[i-1]+2, str(y_list[i-1]), fontweight='bold', ha='center', rotation=90)


    plt.show()
    #plt.savefig('ino_repeats.pdf')













































if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot distribution of repeat elements")
    parser.add_argument("file_path1", type=str, help="Enter file path.", nargs='?')
    args = parser.parse_args()

plot_repeats(args.file_path1)




