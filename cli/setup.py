
from setuptools import setup, find_packages
from datapane.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='datapane',
    version=VERSION,
    description='The quickest way to share datasets and results.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Ajat Prabha',
    author_email='ajat.prabha.leo@gmail.com',
    url='https://github.com/ajatprabha/be-hiring-challenge/',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'datapane': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        datapane = datapane.main:main
    """,
)
