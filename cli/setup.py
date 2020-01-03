from setuptools import setup

setup(
    name='datapane-cli',
    version='1.0',
    py_modules=['datapane-cli'],
    install_requires=[
        'click',
        'pandas',
        'requests'
    ],
    entry_points="""
        [console_scripts]
        datapane-cli=cli:cli
    """
)
