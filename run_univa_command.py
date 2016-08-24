#!/usr/bin/env python

""" Runs UNIVA command on UGE cluster and generate XML file for other functions to process data. """

import subprocess
import logging
import shlex
from uge_environ import add_environment_vars

LOG = logging.getLogger("")
logfile = "/var/log/messages" 

logging.basicConfig(filename=logfile,level=logging.DEBUG, format='%(asctime)s: %(levelname)s - %(message)s', datefmt = '%b %e %H:%M:%S')

def run_univa_commands(univa_command):
    """ Run UNIVA commands.
    Expects a set, [0] is the command. [1] is the output path for the XML file."""

    with open(univa_command[1], 'w') as univa_output_fp:
        LOG.info("run_univa_commands : Getting `{0}` results - Trying".format(univa_command[0]))
        try:
            univa_command_result = subprocess.Popen(shlex.split(univa_command[0]), stdout = univa_output_fp)
        except Exception, e:
            # Unable to get results for {univa_command}.
            LOG.fatal("run_univa_commands : Command - '%s' - raised error: returncode: %s, output: %s" % (e.cmd, e.returncode, e.output))
            LOG.fatal("run_univa_commands : Unable to get results for `{0}`. Maybe qmaster is down?".format(univa_command[0]))
        else:
            univa_output_fp.close()
            LOG.info("`run_univa_commands : {0}` results have been written.".format(univa_command[0]))

    return True

def main():
    """ Main function, you're not supposed to call this function if you import this script from check_uge.py, call run_univa_commands() directly, the following lines of code serves as an example on what sort of datatype to pass into run_univa_commands(). """

    dictofugecommands = {"qhost -q -xml": "/usr/local/bin/scripts/qhost-q_xml.xml", "qstat -u \'*\' -xml": "/usr/local/bin/scripts/qstat_all_users.xml"}

    for ugecommand in dictofugecommands.iteritems():
        run_univa_commands(ugecommand)

if __name__ == '__main__':
    main()
