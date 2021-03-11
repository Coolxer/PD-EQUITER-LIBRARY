
import pathlib
from setuptools import setup, find_packages

NAME = 'equiter'
VERSION = '0.0.1'
AUTHOR = 'Łukasz Miłoś'
EMAIL = "lukasz.milos@int.pl"
URL = 'https://github.com/Coolxer/Equiter--CODE'

DESCRIPTION = 'Equiter - biblioteka funkcji iteracyjnych rozwiązywania układów równań liniowych'
LONG_DESCRIPTION = ("README.md").read_text()

REQUIRED = [
    'numpy',
    'matplotlib',
    'pytest',
    'tabulate'
]

KEYWORDS = [
    'equiter',
    'equations',
    'jacobi',
    'gauss',
    'seidel',
    'sor',
    'cg',
    'bi cg stab',
    'gm res'
]


# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    # add any additional packages that
    install_requires=REQUIRED,
    # needs to be installed along with your package. Eg: 'caer'

    keywords=KEYWORDS,
)
