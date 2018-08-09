#!/usr/bin/python -tt
# Script for removal of reads that contribute to the formation of organeles
from Bio import SeqIO

import argparse

# Read and parse the arguments from the command line
parser =  argparse.ArgumentParser()
parser.add_argument('-v', '--version', action='version', version='Version 0.6')
parser.add_argument('--select', help='Remove or select for reads', action='store_true')
parser.add_argument('original_fasta', help='location of FASTA file')
parser.add_argument('in_file', help='PAF or text file with sequence names')
parser.add_argument('out_file', help='filename for output of sequences')
args = parser.parse_args()

input_handle = open(args.in_file, 'rU')
output_handle = open(args.out_file, 'w')

identifiers = []

# Read in sequence names from a PAF file generated by Rebaler
for line in input_handle:
	# For PAF uncomment following line
	#seq_name = line.split('\t')
	seq_name = line.split('\n')
	identifiers.append(seq_name[0])
#print(identifiers)
records = SeqIO.parse(args.original_fasta, 'fasta')
for record in records:
	if args.select:
		if record.id in identifiers:
			SeqIO.write(record, output_handle, 'fasta')
	else:
		if record.id not in identifiers:
			SeqIO.write(record, output_handle, 'fasta')
