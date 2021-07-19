import os
from setuptools import setup

thelibFolder = os.path.dirname(os.path.realpath(__file__))
paths = ['inference/requirements.txt', 'frontend/requirements.txt']
install_requires = []
for requirementPath in paths:
	if os.path.isfile(requirementPath):
			with open(requirementPath) as f:
					install_requires.extend(f.read().splitlines())

setup(name="yourpackage", install_requires=install_requires)