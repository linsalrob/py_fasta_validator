"""
Some example validation code
"""

import argparse

from PyFastaValidator import validate_fasta_file

__author__ = 'Rob Edwards'
__copyright__ = 'Copyright 2020, Rob Edwards'
__credits__ = ['Rob Edwards']
__license__ = 'MIT'
__maintainer__ = 'Rob Edwards'
__email__ = 'raedwards@gmail.com'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=' ')
    parser.add_argument('-f', help='input file', required=True)
    args = parser.parse_args()

    r = 0
    try:
        r = validate_fasta_file(args.f)
    except Exception as e:
        print(f"Recieved the error {e.message} from {type(e)}")
    print(f"{args.f} returned {r}")

