# Overview
This project contains a python script that will analyze the data file provided
and output the host metrics as requested.

The script was written for Python 2.7 and can be run with a standard Python 2.7
distro via:

```
./main.py -f <path_to_data_file>

# where <path_to_data_file> is the host metrics data file
```

# Setting up Python environment to run BDD tests
This script was developed using BDD via the python equivalent of Cucumber
called 'lettuce'.  Also, PyBuilder was used to build the project and run
the BDD tests.  PyBuilder is a maven-like tool for Python.

These tools require your Python 2.7 environment to have some additional
dependencies installed.  A Dockerfile was created that will provide an appropriate
Python environment for trying out the tests.

With 'docker' installed, you can run the following commands to run PyBuilder
and the BDD tests:

```
git clone git@github.com:matthem78/example.git
cd example
docker build -t matthewm78/example .
docker run -v $(pwd):/example -it matthewm78/example /bin/bash

# From inside container
cd /example

# Install dependencies required to allow PyBuilder to run BDD tests
pyb install_dependencies

# Run BDD tests
pyb -v

# Optionally: run the script against the provided data file
src/main/python/analyzer/main.py -f mt_test_data.txt
```

