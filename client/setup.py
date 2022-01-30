#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['Click>=8.0', "requests>=2.0,<3.0", "pydantic>=1.9,<2.0"]

test_requirements = ['pytest>=3', ]

setup(
    author="Ivan",
    author_email='ivan@mail.com',
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python API client",
    entry_points={
        'console_scripts': [
            'datapane-client=client.cli:cli',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n',
    include_package_data=True,
    keywords='datapane-client',
    name='datapane-client',
    packages=find_packages(include=['client', 'client.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ivan-ah/be-hiring-challenge',
    version='0.1.0',
    zip_safe=False,
)
