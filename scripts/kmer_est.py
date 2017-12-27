## Fast and dirty script for generating kmer files via jellyfish

# Read arguments from the commandline
import argparse
# Import OS to run external programs
import os
import glob

def csv_list(string):
   return string.split(',')

# Read and parse the arguments from the command line
parser =  argparse.ArgumentParser()
parser.add_argument('-v', '--version', action = 'version', version = 'Version 0.1')
parser.add_argument('filename', help = 'location of FASTQ file')
parser.add_argument('kmer', help = 'kmer lengths to test, comma separated', type = csv_list)
args = parser.parse_args()

fastq_handle = args.filename
kmer_length = []
kmer_length = args.kmer

trim = len(kmer_length)
for files in range(trim):
	# Run jellyfish
	kmer_out = str(kmer_length[files]) + '_mer.txt'
	histo_out = 'histo' + str(kmer_length[files]) + '_mer.txt'
	print('Running %s') % (kmer_out)
	# For transcriptome data remove the -C (since it is single end)
	os.system('jellyfish count -t 4 -m %s -s 5G -o %s %s' % (kmer_length[files], kmer_out, fastq_handle))
	os.system('jellyfish histo -t 4 -o %s %s' % (histo_out, kmer_out))
