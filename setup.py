from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Navi Pro',
    version="5.0.3",
    description="A command-line interface to Tenable.io",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Casey Reid",
    author_email="itprofguru@gmail.com",
    url="https://github.com/packetchaos/Navi",
    license="GNUv3",
    keywords='tenable tenable_io navi tio, lumin, navi pro, tio cli, tenable io cli',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'Click>=7.0',
        'requests',
        'pprint>=0.1'
    ],
    python_requires='>=3.0',
    extras_require={
    },
    entry_points={
        'console_scripts': [
            'Navi=Navi.cli:cli',
        ],
    },
)

