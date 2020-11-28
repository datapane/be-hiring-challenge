from setuptools import setup

setup(
    name='datasets',
    description='Dataset CLI',
    version='0.1',
    py_modules=['dataset'],
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        dataset=main:cli
    ''',
)
