#!/usr/bin/env python

import os

"""
This script adds environment variables to the environment the python scripts requesting data from the UGE cluster runs in.

Below are the BASH equivalent we familiar with, without them, UNIVA commands will not run.

    export SGE_ROOT=/path/to/uge-8.1.7p3
    export SGE_CELL=cell_name
    export SGE_CLUSTER_NAME=cluster_name
    export PATH=/path/to/uge-8.1.7p3/bin/lx-amd64/:$PATH

Note: In order for the machine submitting UNIVA commands, it needs to be either a SUBMISSION HOST or a ADMINISTRATIVE HOST. This script resides in DLMN03V, which is an ADMINISTRATIVE HOST. To allow another host to be a ADMINISTRATIVE HOST or SUBMISSION HOST, run `qconf -ah` or `qconf -as` accordingly.
"""

def add_environment_vars():
    """ Adds environment variables for UGE. """

    SGE_ROOT = '/path/to/uge-8.1.7p3'
    SGE_CELL = 'cell_name'
    SGE_CLUSTER_NAME = 'cluster_name'
    SGE_PATH = '/path/to/uge-8.1.7p3/bin/lx-amd64/'

    os.environ['SGE_ROOT'] = SGE_ROOT
    os.environ['SGE_CELL'] = SGE_CELL
    os.environ['SGE_CLUSTER_NAME'] = SGE_CLUSTER_NAME
    os.environ['PATH'] = SGE_PATH + os.pathsep + os.environ['PATH']

    os.environ()

    return True
