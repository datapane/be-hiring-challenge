from setuptools import setup

setup(
    name='Datapane',
    version='1.0',
    py_modules=['datapane'],
    include_package_data=True,
    install_requires=[
        'click',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        datapane=datapane:cli
    ''',
)