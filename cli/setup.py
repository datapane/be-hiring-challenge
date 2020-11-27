import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'datapane-cli'
AUTHOR = 'Sanket Mokashi'
AUTHOR_EMAIL = 'sanketm21995@email.com'
URL = 'https://github.com/you/your_package'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Describe your package in one sentence'

INSTALL_REQUIRES = [
      'pandas',
      'fsspec',
      'xlwt',
      'matplotlib'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(),
      entry_points="""
        [console_scripts]
        datapane=commands.commands:cli
    """,
      )