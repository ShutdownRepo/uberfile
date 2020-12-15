import shutil
from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    requirements = [x.strip() for x in content]

shutil.copyfile('uberfile.py', 'uberfile')

setup(
    name='uberfile',
    version='1.0.0',
    author='Shutdown & en1ma',
    description='Simple CLI tool for the generation of downloader oneliners for UNIX-like or Windows systems',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ShutdownRepo/uberfile',
    classifiers=[
        'Environment :: Console'
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    scripts=['uberfile']
