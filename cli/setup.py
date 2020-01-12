from setuptools import setup

setup(
    name="dataset-cli",
    version='1.0',
    py_modules=['cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        dataset-cli=cli:cli
    ''',
)
