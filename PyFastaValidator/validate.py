"""
Validate a fasta file or except with the appropriate code.
"""

import sys
import argparse

from PyFastaValidator import validate_fasta_file, __version__


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
        try:
            r = validate_fasta_file(args.f)
        except Exception as e:
            print(f"Recieved the error {e} from {type(e)}")
        print(f"Exiting with code {r}")
        sys.exit(r)
    else:
        print(f"{sys.argv[0]} version {__version__}")
