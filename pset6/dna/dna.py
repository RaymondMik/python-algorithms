import csv
from sys import argv
from itertools import groupby
import re

def matchDNA():
    #open csv and sequences file and write those into memory
    STRs = []
    LIST_OF_SUSPECTS = {}

    with open(argv[1]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        lines = 0
        for row in csv_reader:
            # get STRs from csv header
            if lines == 0:
                row.remove("name");
                STRs = row
            else:
                name = row.pop(0)
                LIST_OF_SUSPECTS[name] = row
            lines += 1

    # open sequencies file and read its content
    file = open(argv[2], "r")
    occurencies = []
    sequence = file.read()
    file.close()

    #calculate the number of times each SRT repeats consecutively in the DNA sequence
    for STR in STRs:
        # https://stackoverflow.com/a/61134156/5748790
        count = 0
        pattern = STR
        while pattern in sequence:
            count += 1
            pattern += STR

        occurencies.append(str(count))

    #compare those accounts against each rows in the sequences DB
    for suspect_name in LIST_OF_SUSPECTS:
        if LIST_OF_SUSPECTS[suspect_name] == occurencies:
            return suspect_name;

    return "No Match"

print(matchDNA())

#22,33,43,12,26,18,47,41
#python dna.py databases/large.csv sequences/5.txt Lavender