import setuptools
from distutils.core import setup, Extension
import os

# Read the markdown files for the long description
def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        if os.path.exists(filename):
            with open(filename, "r", encoding=encoding) as f:
                buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')

def get_version():
    with open("VERSION", 'r') as f:
        v = f.readline().strip()
        return v


setup(
    name='py_fasta_validator',
    version=get_version(),
    packages=setuptools.find_packages(),
    url='https://github.com/linsalrob/py_fasta_validator',
    license='The MIT License (MIT)',
    author='Rob Edwards',
    author_email='raedwards@gmail.com',
    description='A small, lightweight, fast fasta validator written in C',
    long_description=long_description,
    long_description_content_type="text/markdown",
    platforms='any',
    keywords="bioinformatics genome genomics fasta",
    ext_modules=[Extension("FastaValidator", sources=["src/fasta_validate.c"], language='c')],
    entry_points={
        "console_scripts": ["py_fasta_validator = PyFastaValidator.validate:validate"]
    },
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.0',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    zip_safe=True,
)

