from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A Python library for running Indic Python Scripts'
LONG_DESCRIPTION = 'A Python library for running Indic Python Scripts written completely in Indian Languages such as Kannada and Hindi. It is a wrapper around the Indic Python Scripts written in the Indic Scripting Language (ISL).'

# Setting up
setup(
	name="indicpy",
	version=VERSION,
	author="Suprad S Parashar",
	author_email="suprad.s.parashar@gmail.com",
	description=DESCRIPTION,
	long_description_content_type="text/markdown",
	long_description=LONG_DESCRIPTION,
	packages=find_packages(),
	install_requires=['argparse', 'tokenize' 'typing'],
	keywords=['python', 'indian', 'local', 'indic', 'dravidian', 'devanagari', 'scripts'],
	classifiers=[
		"Development Status :: 1 - Planning",
		"Intended Audience :: Developers",
		"Programming Language :: Python :: 3",
		"Operating System :: Unix",
		"Operating System :: MacOS :: MacOS X",
		"Operating System :: Microsoft :: Windows",
	]
)