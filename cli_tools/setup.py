from setuptools import setup

setup(
    name="cli-tools",
    version='1.0',
    description='CLI tool to interact with dataset api-server',
    author='Nishant Suman',
    author_email='nishant.suman23@gmail.com',
    py_modules=['cli_tools'],
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        cli-tools=cli_tools:cli
    ''',
)