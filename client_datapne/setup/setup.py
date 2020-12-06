from setuptools import setup

setup(
   name='cfetch',
   version='0.1.0',
   author='An Awesome Coder',
   author_email='aac@example.com',
   packages=['cfetch'],
   scripts=['cfetch/cfetch.py'],
   install_requires=[
       "requests",
   ],
)


