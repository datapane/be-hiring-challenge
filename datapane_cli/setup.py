from setuptools import setup

setup(
    name='datasetcli',
    version='0.1',
    py_modules=['commands'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        datasetcli=commands:cli
    ''',
)