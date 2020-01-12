from setuptools import setup

setup(
    name="dataset-cli",
    version='1.0',
    description='CLI tool to interact with dataset server',
    author='Aniket Dokania',
    author_email='anidok2008@gmail.com',
    py_modules=['cli'],
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        dataset-cli=cli:cli
    ''',
)
