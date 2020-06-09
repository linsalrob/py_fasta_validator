"""
Validate a fasta file
"""

import os
import sys
import argparse

import FastaValidator
from .exceptions import FirstCharacterIncorrect, DuplicateIdentifiers, NonSequenceCharacters

__author__ = 'Rob Edwards'


def validate_fasta_file(fname):
    """
    Validate the fasta file

    We raise an exception if the file is not valid to demonstrate how to report errors

    :param fname: the file name
    :return: the code returned by the validator
    """

    rc = FastaValidator.fasta_validator(fname)

    if rc == 1:
        raise FirstCharacterIncorrect(f"{fname} does not start with a >")
    if rc == 2:
        raise DuplicateIdentifiers(f"{fname} has multiple sequences with the same identifier")
    if rc == 4:
        raise NonSequenceCharacters(f"{fname} has non-sequence characters in it")

    return rc





