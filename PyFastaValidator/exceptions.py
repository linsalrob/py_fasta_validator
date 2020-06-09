"""
A custom error class for fasta validator
"""
class Error(Exception):
    """
    Base class for exceptions in this module.
    """
    pass

"""
The errors associated with fasta validator are:

* `0` this is a valid fasta file
* `1` the first line does not start with a > (rule 1 violated).
* `2` there are duplicate sequence identifiers in the file (rule 7 violated)
* `4` there are characters in a sequence line other than [A-Za-z]

"""

class FirstCharacterIncorrect(Error):
    """
    Exception raised for the first line not starting with a >.
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class DuplicateIdentifiers(Error):
    """
    There are duplicate sequence identifiers in the file (rule 7 violated)
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NonSequenceCharacters(Error):
    """
    there are characters in a sequence line other than [A-Za-z]
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)