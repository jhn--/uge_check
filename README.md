# uge_check
Runs qhost -q -xml and check for high load avg/mem usage compute nodes and down nodes. Works on UGE 8.1.7p3.

Simple bunch of python 2.6 scripts which runs UNIVA commands, retrieves XML output, checks for high load or down nodes and generates HTML file.

Basically this is a quick and dirty job to check if there's anything wrong w/ the nodes in the UGE cluster.
The flow of the programs work like this -
Cron daemon runs in an interval -
  Executes 'check_uge.py -cu' to generate XML output files, check_uge.py has a dictionary of UNIVA commands and the corresponding XML out file location, check_uge.py will call run_univa_commands.py to run subprocess UNIVA commands, which in turns, executes univa_environ.py to export UGE environment variables in order to run UNIVA commands.
Cron daemon runs in separate intervals -
  Executes 'check_uge.py -hl' to parse the same XML file for high 'np_load_avg'(> 0.8) or high 'mem_used' ((mem_used/mem_total)*100 >= 80.0) or both, picks out nodes and pushes to writeout.py for HTML file generation.
  
  Executes 'check_uge.py -ooc' to parse the same output XML file for dash (-), in 'np_load_avg' field, which stands for node is down (if sgeexecd in compute node doesn't run, qmaster will not get health stats and thus will generate'-'), picks out nodes and pushes to writeout.py for separate HTML file generation.
  If there are any nodes with '-', will send an email to admins using the same HTML file generated earlier.

The running of UGE commands is separated from the checking of nodes with issues (heavy load or down) from the XML file(s), hence the -cu, -hl and -ooc arguments. Run webserver to show generated HTML files with HTML boilerplates e.g. initializr.

Some user actions required - 

univa_environ.py
Enter the $SGE values for commands to work.

run_univa_commands.py
-none-

check_uge.py
Output XML files will be placed in /usr/local/bin/scripts. Why? Because that's where the python scripts originally are.
dictofugecommands = {
    "qhost -q -xml": "/usr/local/bin/scripts/qhost-q.xml", 
    "qstat -u \'*\' -xml": "/usr/local/bin/scripts/qstat_all_users.xml"
    }

writeout.py
Location of two generated HTML files, I used initializr as a boilerplate, hence the path.
nwhru_html = '/var/www/html/initializr/nodes_with_high_resource_usage.html'
nooc = '/var/www/html/initializr/nodes_out_of_circulation.html'

send_email.py
Notifies recipients when nodes got taken out of circulation.
Change 'recipients' and 'sender' variables with legitimate email addresses.
smtp server also needs to change (unless you're really using localhost).
smtpserver = smtplib.SMTP('localhost')
Sends writeout.py-generated HTML file
nooc = '/var/www/html/initializr/nodes_out_of_circulation.html'

Hope to port this to Flask.
