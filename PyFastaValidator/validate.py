"""
Validate a fasta file or except with the appropriate code.
"""

import sys
import argparse

from PyFastaValidator import __version__, \
import FastaValidator



def validate():
    """
    Validate a fasta file
    """
    parser = argparse.ArgumentParser(description='Validate a fasta file')
    parser.add_argument('-f', '--file', help='fasta file to validate')
    parser.add_argument('-v', '--version', help='print the version', action='store_true')
    args = parser.parse_args()

    if args.file:
        r = 0
        rc = FastaValidator.fasta_validator(args.file)

        if rc == 1:
            sys.stderr.write(f"{args.file} does not start with a >\n")
        if rc == 2:
            sys.stderr.write(f"{args.file} has multiple sequences with the same identifier\n")
        if rc == 4:
            sys.stderr.write(f"{args.file} has non-sequence characters in it\n")
            sys.exit(rc)
        else:
            print(f"{sys.argv[0]} version {__version__}")
