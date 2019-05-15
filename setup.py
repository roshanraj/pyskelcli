""" Setup file.
"""
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

README = "python cli"

requires = [
    'tensorflow'
]

setup(name='cli',
    version=0.1,
    description='general description',
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Script :: Utils",
        "Topic :: Script :: Utils :: Application"
    ],
    keywords="utils database postgres",
    author='xavient',
    author_email='',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points="""\
    [console_scripts]
    skelcli = skelcli:main
    skeltest = skelcli.test:printHello
    """,
)

