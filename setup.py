from setuptools import setup, find_packages
from codecs import open
from os import path

file_path = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(file_path, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='newsapi',

    version='0.1.0',

    description='A python wrapper for News API (newsapi.org)',
    long_description=long_description,

    url='https://github.com/slapbot/newsapi',

    author='Ujjwal Gupta',
    author_email='ugupta41@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Environment :: Web Environment',
        'Environment :: Console Environment',

        'Operating System :: OS Independent',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='pynewsapi newsapi newsapi.org news api-client news-feed newsfeeder',

    packages=find_packages(exclude=['sample']),

    install_requires=['requests'],
)
