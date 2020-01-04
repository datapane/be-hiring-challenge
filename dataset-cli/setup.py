from setuptools import setup


f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='dataset-cli',
    version='1.0',
    description='Command line tool to manage Datasets',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Maksudul Haque',
    author_email='saad.mk112@gmail.com',
    url='https://github.com/saadmk11/be-hiring-challenge/tree/challenge',
    license='MIT',
    py_modules=['dataset-cli'],
    install_requires=[
        'click',
        'requests'
    ],
    entry_points="""
        [console_scripts]
        dataset-cli=cli:api
    """
)
