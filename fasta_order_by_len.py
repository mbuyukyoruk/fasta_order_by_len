import argparse
import re
import sys
import subprocess
import os
import textwrap

try:
    from Bio import SeqIO
except:
    print("SeqIO module is not installed! Please install SeqIO and try again.")
    sys.exit()

try:
    import tqdm
except:
    print("tqdm module is not installed! Please install tqdm and try again.")
    sys.exit()

parser = argparse.ArgumentParser(prog='python fasta_order_by_len.py',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=textwrap.dedent('''\

# fasta_order_by_len

Author: Murat Buyukyoruk

        fasta_order_by_len help:

This script is developed to order sequences in a multifasta file by the length of sequences.

SeqIO package from Bio is required to fetch flank sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.

Syntax:

        python fasta_order_by_len.py -i demo.fasta

fasta_unalignr dependencies:

Bio module and SeqIO available in this package          refer to https://biopython.org/wiki/Download
	
tqdm                                                    refer to https://pypi.org/project/tqdm/

Input Paramaters (REQUIRED):
----------------------------
	-i/--input		FASTA			Specify a fasta file.

	-o/--output		FASTA			Specify a fasta file.

Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.

      	'''))
parser.add_argument('-i', '--input', required=True, type=str, dest='filename', help='Specify a fastafile.\n')

parser.add_argument('-o', '--output', required=True, dest='out', help='Specify a output fasta file name.\n')

results = parser.parse_args()
filename = results.filename
out = results.out

os.system('> ' + out)

seq_list = []
seq_desc_list = []
seq_len = []

proc = subprocess.Popen("grep -c '>' " + filename, shell=True, stdout=subprocess.PIPE, text=True)
length = int(proc.communicate()[0].split('\n')[0])

with tqdm.tqdm(range(length)) as pbar:
    pbar.set_description('Reading fasta...')
    for record in SeqIO.parse(filename, "fasta"):
        pbar.update()
        seq_desc_list.append(record.description)
        seq_list.append(record.seq)
        seq_len.append(len(record.seq))

length = max(seq_len)

with tqdm.tqdm(range(length + 1)) as pbar:
    pbar.set_description('Ordering fasta...')
    for i in reversed(range(length + 1)):
        pbar.update()
        for l in range(len(seq_list)):
            if len(seq_list[l]) == i:
                f = open(out, 'a')
                sys.stdout = f
                print(">" + seq_desc_list[l])
                print(re.sub("(.{60})", "\\1\n", str(seq_list[l]), 0, re.DOTALL))