#!/usr/bin/env python

import datetime

datetimenow = str(datetime.datetime.now())

def write_to_high_resource(input_data):
    """ Accepts dictionary and publishes HTML file. """

    # Destination HTML file.
    nwhru_html = '/var/www/html/initializr/nodes_with_high_resource_usage.html'

    # If there are any nodes under heavy load, the length of the dictionary will not be 0.
    if len(input_data) > 0:
        try:
            nwhru_fp =  open(nwhru_html, 'w')
        except Exception, e:
            print(e)
        else:
            nwhru_fp.write("<table width=\"100%\">")
            nwhru_fp.write("<tr>")
            nwhru_fp.write("<th>")
            nwhru_fp.write("Date and time of update: ")
            nwhru_fp.write("</th>")
            nwhru_fp.write("<th>")
            nwhru_fp.write(datetimenow)
            nwhru_fp.write("</th>")
            nwhru_fp.write("</tr>")
            nwhru_fp.write("<tr><th>Nodes under high resource usage:</th></tr>")
            nwhru_fp.write("<tr><th>Node</th><th>arch_string</th><th>swap_used</th><th>num_proc</th><th>swap_total</th><th>m_core</th><th>mem_used</th><th>m_socket</th><th>mem_total</th><th>np_load_avg</th></tr>")
            for node in input_data:
                nwhru_fp.write("<tr>")
                nwhru_fp.write("<td>")
                nwhru_fp.write(node)
                nwhru_fp.write("</td>")
                nwhru_fp.write("<td>")
                nwhru_fp.write(input_data[node]['arch_string'])
                nwhru_fp.write("</td>")
                nwhru_fp.write("<td>")
                nwhru_fp.write(input_data[node]['swap_used'])
                nwhru_fp.write("</td>")
                nwhru_fp.write("<td>")
                nwhru_fp.write(input_data[node]['num_proc'])
                nwhru_fp.write("</td>")
                nwhru_fp.write("<td>")
                nwhru_fp.write(input_data[node]['swap_total'])
                nwhru_fp.write("</td>")
                nwhru_fp.write("<td>")
                nwhru_fp.write(input_data[node]['m_core'])
                nwhru_fp.write("</td>")
                nwhru_fp.write("<td>")
                nwhru_fp.write(input_data[node]['mem_used'])
                nwhru_fp.write("</td>")
                nwhru_fp.write("<td>")
                nwhru_fp.write(input_data[node]['m_socket'])
                nwhru_fp.write("</td>")
                nwhru_fp.write("<td>")
                nwhru_fp.write(input_data[node]['mem_total'])
                nwhru_fp.write("</td>")
                nwhru_fp.write("<td>")
                nwhru_fp.write(input_data[node]['np_load_avg'])
                nwhru_fp.write("</td>")
                nwhru_fp.write("</tr>")
            nwhru_fp.write("</table>")
        finally:
            nwhru_fp.close()
    else:
        try:
            nwhru_fp =  open(nwhru_html, 'w')
        except Exception, e:
            print(e)
        else:
            nwhru_fp.write("<table width=\"100%\">")
            nwhru_fp.write("<tr>")
            nwhru_fp.write("<th>")
            nwhru_fp.write("Date and time of update: ")
            nwhru_fp.write("</th>")
            nwhru_fp.write("<th>")
            nwhru_fp.write(datetimenow)
            nwhru_fp.write("</th>")
            nwhru_fp.write("</tr>")
            nwhru_fp.write("<tr>")
            nwhru_fp.write("<td>")
            nwhru_fp.write("<h2>No nodes under heavy load.</h2>")
            nwhru_fp.write("</td>")
            nwhru_fp.write("</tr>")
            nwhru_fp.write("</table>")
        finally:
            nwhru_fp.close()
            return True

def write_to_ooc(input_data):
    """ Accepts dictionary and publishes HTML file. """

    # Destination HTML file.
    nooc = '/var/www/html/initializr/nodes_out_of_circulation.html'
    
    # If there are any nodes under heavy load, the length of the dictionary will not be 0.
    if len(input_data) > 0:
        try:
            nooc_fp =  open(nooc, 'w')
        except Exception, e:
            print(e)
        else:
            nooc_fp.write("<table width=\"100%\">")
            nooc_fp.write("<tr>")
            nooc_fp.write("<th>")
            nooc_fp.write("Date and time of update: ")
            nooc_fp.write("</th>")
            nooc_fp.write("<th>")
            nooc_fp.write(datetimenow)
            nooc_fp.write("</th>")
            nooc_fp.write("</tr>")
            nooc_fp.write("<tr><th>Nodes out of circulation:</th></tr>")
            nooc_fp.write("<tr><th>Node</th><th>arch_string</th><th>swap_used</th><th>num_proc</th><th>swap_total</th><th>m_core</th><th>mem_used</th><th>m_socket</th><th>mem_total</th><th>np_load_avg</th></tr>")
            for node in input_data:
                nooc_fp.write("<tr>")
                nooc_fp.write("<td>")
                nooc_fp.write(node)
                nooc_fp.write("</td>")
                nooc_fp.write("<td>")
                nooc_fp.write(input_data[node]['arch_string'])
                nooc_fp.write("</td>")
                nooc_fp.write("<td>")
                nooc_fp.write(input_data[node]['swap_used'])
                nooc_fp.write("</td>")
                nooc_fp.write("<td>")
                nooc_fp.write(input_data[node]['num_proc'])
                nooc_fp.write("</td>")
                nooc_fp.write("<td>")
                nooc_fp.write(input_data[node]['swap_total'])
                nooc_fp.write("</td>")
                nooc_fp.write("<td>")
                nooc_fp.write(input_data[node]['m_core'])
                nooc_fp.write("</td>")
                nooc_fp.write("<td>")
                nooc_fp.write(input_data[node]['mem_used'])
                nooc_fp.write("</td>")
                nooc_fp.write("<td>")
                nooc_fp.write(input_data[node]['m_socket'])
                nooc_fp.write("</td>")
                nooc_fp.write("<td>")
                nooc_fp.write(input_data[node]['mem_total'])
                nooc_fp.write("</td>")
                nooc_fp.write("<td>")
                nooc_fp.write(input_data[node]['np_load_avg'])
                nooc_fp.write("</td>")
                nooc_fp.write("</tr>")
            nooc_fp.write("</table>")
        finally:
            nooc_fp.close()
    else:
        try:
            nooc_fp =  open(nooc, 'w')
        except Exception, e:
            print(e)
        else:
            nooc_fp.write("<table width=\"100%\">")
            nooc_fp.write("<tr>")
            nooc_fp.write("<th>")
            nooc_fp.write("Date and time of update: ")
            nooc_fp.write("</th>")
            nooc_fp.write("<th>")
            nooc_fp.write(datetimenow)
            nooc_fp.write("</th>")
            nooc_fp.write("</tr>")
            nooc_fp.write("<tr>")
            nooc_fp.write("<td>")
            nooc_fp.write("<h2>All nodes are operational.</h2>")
            nooc_fp.write("</td>")
            nooc_fp.write("</tr>")
            nooc_fp.write("</table>")
        finally:
            nooc_fp.close()
            return False
