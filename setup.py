import os
from setuptools import setup, find_packages

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'README.rst')

setup(
    name='django-cms-feed-generator',
    version='0.0.9',
    description='RSS feed generator plugin for Django CMS',
    long_description = open(README_PATH, 'r').read(),
    author='PBS Audience Facing Team',
    author_email='tpg-pbs-userfacing@threepillarglobal.com',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
)
