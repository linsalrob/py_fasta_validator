"""
Validate a fasta file or except with the appropriate code.
"""

import sys
import argparse

from PyFastaValidator import validate_fasta_file


def validate():
    """
    Validate a fasta file
    """
    parser = argparse.ArgumentParser(description='Validate a fasta file')
    parser.add_argument('-f', help='fasta file to validate', required=True)
    args = parser.parse_args()

    r = 0
    try:
        r = validate_fasta_file(args.f)
    except Exception as e:
        print(f"Recieved the error {e} from {type(e)}")
    print(f"Exiting with code {r}")
    sys.exit(r)
