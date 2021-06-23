[![Edwards Lab](https://img.shields.io/badge/Bioinformatics-EdwardsLab-03A9F4)](https://edwards.flinders.edu.au)
[![DOI](https://www.zenodo.org/badge/270903677.svg)](https://www.zenodo.org/badge/latestdoi/270903677)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub language count](https://img.shields.io/github/languages/count/linsalrob/py_fasta_validator)
[![PyPi](https://img.shields.io/pypi/pyversions/py-fasta-validator.svg?style=flat-square&label=PyPi%20Versions)](https://pypi.org/project/py-fasta-validator/)
[![Downloads](https://img.shields.io/github/downloads/linsalrob/py_fasta_validator/total?style=flat-square)](https://github.com/linsalrob/py_fasta_validator/releases)

# py_fasta_validator

A Python extension of the [fasta validator](https://github.com/linsalrob/fasta_validator)

This is a Python C-extension to validate a fasta file. It only checks a few things, and by default only sets its response via the return code, so you will need to check that in your Python code. See the examples provided.

The simple rules that we adhere to are:

1. Each header line starts with a `>`. The header preceedes the sequence.
2. Every other line is considered a sequence line
3. Sequence lines may not contain whitespace, numbers, or non-sequence characters. In other words, they must only contain the characters [A-Z] and [a-z]
4. Sequence lines can end with a new line or return depending on whether you have edited this file on a mac, pc, or linux machine.
5. Sequence lines can be empty.
6. The sequence identifier is the string of characters in the header line following the `>` and upto the first whitespace. Everything after the first whitespace is descriptive, and can be as long as you like
7. Each sequence identifier must be unique within the fasta file.

We will exit with the following return codes:

* `0` this is a valid fasta file
* `1` the first line does not start with a > (rule 1 violated).
* `2` there are duplicate sequence identifiers in the file (rule 7 violated)
* `4` there are characters in a sequence line other than [A-Za-z]

Other exit codes (e.g. 255, 254, etc) indicate internal errors in the program.

# Running py_fasta_validator

The installation now also includes a command line application, `py_fasta_validator` that you can run. See the Testing section below!

You can also import FastaValidator directly:

```python
import FastaValidator

return_code = FastaValidator.fasta_validator(file_name)
```

# Installation

### Everyone

_Recommended:_

Install with conda. This is the easiest way to install `py_fasta_validator` and the recommended method:

```command-line
conda install -c bioconda py_fasta_validator
```

_Alternate method:_

Install with pip:

```
pip install py-fasta-validator
```

### Advanced

#### Prerequisites

If you install using one the methods above you don't need to worry about the prerequistes, they are already included!

[fasta validator](https://github.com/linsalrob/fasta_validator) is written in ANSI C but you will also need the Python developers toolkit (e.g. python-3.x-dev installed on your machine to provide Python.h)


To clone the code from GitHub use:

```bash
git clone https://github.com/linsalrob/fasta_validator.git
cd fasta_validator
```

To build the code, use:

```bash
make
```

This should compile the source into an executable in the current working directory.

Please note, if you get an error like this:

```
gcc  -Wall -o fasta_validate ./fasta_validate.c -I/usr/include/python3.8 -I/usr/include/x86_64-linux-gnu/python3.8
/usr/bin/ld: /tmp/ccgvrFaq.o: in function `python_input':
fasta_validate.c:(.text+0x481): undefined reference to `PyArg_ParseTuple'
/usr/bin/ld: fasta_validate.c:(.text+0x48c): undefined reference to `PyExc_RuntimeError'
/usr/bin/ld: fasta_validate.c:(.text+0x49b): undefined reference to `PyErr_SetString'
/usr/bin/ld: fasta_validate.c:(.text+0x4c3): undefined reference to `PyLong_FromLong'
/usr/bin/ld: /tmp/ccgvrFaq.o: in function `PyInit_fastaValidator':
fasta_validate.c:(.text+0x4f2): undefined reference to `PyModule_Create2'
collect2: error: ld returned 1 exit status
make: *** [Makefile:9: all] Error 1
```

Then we need to append the version of python to the `make` command. I am (currently) running `python3.8` and the command to compile without error is:

```
make CFLAGS=-lpython3.8
```

<small>I don't know the exact cause of this error, but `pkg-config --libs python3` is not reporting anything when it should report `-lpython3.8`</small>

To install this code as root (sudo) you can use:

```bash
make install
```

and this will copy the executable to `/usr/local/bin`.

to install it as a user, just copy the compiled binary `fasta_validate` to somewhere on your path.


# Testing

To test the code you can use the example data provided. Download the [test data set](https://github.com/linsalrob/py_fasta_validator/raw/master/test.zip) [zip file, 16.4 kb] and uncompress it.

```command-line
$ for FASTA in test/*fasta; do echo $FASTA; py_fasta_validator -f $FASTA; echo "Exit code: $?"; done
```

This will output the name of the fasta file, the output, and the exit code from the process:

```command-line
test/code.fasta
test/code.fasta has non-sequence characters in it
Exit code: 4
test/duplicates_no_spaces.fasta
test/duplicates_no_spaces.fasta has multiple sequences with the same identifier
Exit code: 2
test/duplicates_with_spaces.fasta
test/duplicates_with_spaces.fasta has multiple sequences with the same identifier
Exit code: 2
test/good.fasta
Exit code: 0
test/good_mixed.fasta
Exit code: 0
test/good_multiline.fasta
Exit code: 0
test/no_first_line.fasta
test/no_first_line.fasta does not start with a >
Exit code: 1
test/space.fasta
test/space.fasta has non-sequence characters in it
Exit code: 4
```


# Citation

Please cite this as 

Edwards, R.A. 2019. fasta_validate: a fast and efficient fasta validator written in pure C. DOI: 10.5281/zenodo.2532044
[![DOI](https://zenodo.org/badge/164130774.svg)](https://zenodo.org/badge/latestdoi/164130774)

# What is the difference between this and [fasta_validator](https://github.com/linsalrob/fasta_validator)?

Not very much!

The original C code was written for the [Search SRA](https://searchsra.org/) project as we wanted to validate fasta files uploaded by users. That code is written in C, and does not require any additional libraries to install.

This version adds the Python hooks, and so it requires the Python development library to be installed. Therefore, we kept them as two separate projects, although you'll notice the C code is essentially the same!

# License

This software is released using the [MIT License](LICENSE)



