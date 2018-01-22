from setuptools import setup, find_packages


import os
import sys

import travelingintelligence


here = os.path.abspath(os.path.dirname(__file__))
setup(
    name='travelingintelligence',
    version=travelingintelligence.__version__,
    url='https://github.com/abailie3/TravelingIntelligence',
    license='MIT',
    packages=find_packages()
)
