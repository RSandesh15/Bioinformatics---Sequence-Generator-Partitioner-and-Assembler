import random

import Bio
from Bio.Seq import Seq
from Bio import SeqIO
from random import shuffle

records = list(SeqIO.parse("ls_orchid.fasta", "fasta"))
print("File Consists of %i Records\n" % len(records))

print("The First Record")
first_record = records[0]
print(repr(first_record.seq))
print(len(first_record), "\n")

print("The Last Record")
last_record = records[-1]
print(repr(last_record.seq))
print(len(last_record))
print("----------------------------------------------------------------------------\n")

chosen_seq = random.choice(records)

print("I . Simulator for Sequence Generator")
print("Randomly Picking Sequence.............\n")
print("Chosen Sequence\n", "ID is", chosen_seq.id)
print(chosen_seq.seq, "\n")

k = int(input("Enter the Number of Set of Sequences You Require\n"))

if k == 3:

    print("Original Sequence")
    print(chosen_seq.seq + "\n")

    def remove_random_character(phrase, n_remove):
        for num in random.sample(range(0, len(phrase)), n_remove):
            phrase = phrase[:num] + '_' + phrase[num + 1:]
        return phrase

    string = chosen_seq.seq
    len_of_seq = float(len(chosen_seq))
    remove_percentage = float(0.2)
    remove_number = int(len_of_seq * remove_percentage)
    new_phrase = remove_random_character(string, remove_number)
    print("Sequence with Probability 0.2p or p/5 ----------> Randomly Delete Nucleotides")
    print(new_phrase + "\n")

    x_prior = str(chosen_seq.seq)
    x_new = x_prior.replace('C', 't', int(len(chosen_seq) * 0.8)).replace('A', 'g', int(len(chosen_seq) * 0.8))
    x_new1 = x_prior.replace('G', 'a', int(len(chosen_seq) * 0.8)).replace('T', 'c', int(len(chosen_seq) * 0.8))
    print("Sequence with Probability 0.8p or 4p/5 ----------> Random Mutation and Nucleotide Replacement")
    print(random.choice([x_new, x_new1]), "\n")

elif k == 1:
    print("Original Sequence")
    print(chosen_seq.seq + "\n")

elif k > 1:

    prob_num = float(input("Enter Desired Probability Between 0 and 1 (Real Number)\n"))
    print("Original Sequence")
    print(chosen_seq.seq + "\n")

    for i in range(k):
        def remove_random_character(phrase, n_remove):
            for num in random.sample(range(0, len(phrase)), n_remove):
                phrase = phrase[:num] + '_' + phrase[num + 1:]
            return phrase
        string = chosen_seq.seq
        len_of_seq = float(len(chosen_seq))
        remove_percentage = float(0.2)
        remove_number = int(len_of_seq * remove_percentage)
        new_phrase = remove_random_character(string, remove_number)
        print("-->Sequence with Probability", prob_num, " ----------> Randomly Delete Nucleotides")
        print(new_phrase)

        def replace_nucleotides():
            prior = str(chosen_seq.seq)
            new = prior.replace('C', 't', int(len(chosen_seq) * prob_num)).replace('A', 'g', int(len(chosen_seq) * prob_num))
            new1 = prior.replace('G', 'a', int(len(chosen_seq) * prob_num)).replace('T', 'c', int(len(chosen_seq) * prob_num))
            print("-->Sequence with Probability", prob_num, " ----------> Random Mutation and Nucleotide Replacement")
            print(random.choice([new, new1]), "\n")
        replace_nucleotides()
else:

    print("Please Check Your Input Again. Error Identified")

print("#########################################################################################################\n")
print(input("Press Enter to Continue"))
print("Done")

# def sliceString(Str, n):
#     parts = len(Str) // n
#     start = 0
#
#     while (start < len(Str)):
#         print(Str[start: start + parts])
#         start += parts
#
# Str = chosen_seq.seq
# print("*******BEFORE MUTATION*******\n")
# sliceString(Str, k)
