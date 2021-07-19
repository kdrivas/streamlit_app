import os

thelibFolder = os.path.dirname(os.path.realpath(__file__))
paths = [thelibFolder + 'inference/requirements.txt', thelibFolder + 'frontend/requirements.txt']
for requirementPath in paths:
	if os.path.isfile(requirementPath):
			with open(requirementPath) as f:
					install_requires = f.read().splitlines()

setup(name="yourpackage", install_requires=install_requires)