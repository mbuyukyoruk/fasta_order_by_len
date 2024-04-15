# fasta_order_by_len

Author: Murat Buyukyoruk

        fasta_order_by_len help:

This script is developed to order sequences in a multifasta file by the length of sequences.

SeqIO package from Bio is required to fetch flank sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain 
long and many sequences.

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

