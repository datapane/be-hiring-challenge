import pathlib
from setuptools import setup, find_packages
import os

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'datapane-cli'
AUTHOR = 'Sanket Mokashi'
AUTHOR_EMAIL = 'sanketm21995@email.com'
URL = 'https://github.com/Mario2334/be-hiring-challenge'

DESCRIPTION = 'Backend API Hiring Challengee'

INSTALL_REQUIRES = [
      'pandas',
      'fsspec',
      'xlwt',
      'matplotlib',
      'click',
      'tinydb',
      'pyarrow',
      'xlwt'
]
setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(),
      entry_points="""
        [console_scripts]
        datapane=commands.commands:cli
    """,
      )