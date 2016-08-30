#!/usr/bin/env python

import datetime

datetimenow = str(datetime.datetime.now())

def write_to_html(write_code, input_data):
    """ Accepts dictionary and publishes HTML file. """
    # write_code defines which data was passed over and which HTML structure to use.
    # 'hl' = seek_heavy_load
    # 'ooc' = seek_ooc_nodes

    HTML_content = []

    # Destination HTML file.
    if write_code == 'hl':
        writeout_html = '/var/www/html/initializr/nodes_with_high_resource_usage.html'
    elif write_code == 'ooc':
        writeout_html = '/var/www/html/initializr/nodes_out_of_circulation.html'

    # If there are any nodes under heavy load, the length of the dictionary will not be 0.
    if len(input_data) == 0:
        HTML_content = [
        "<tr><td>", 
        "<h2>No nodes under heavy load.</h2>",
        "</td></tr>" 
        ]
    else:
        if write_code == 'hl':
            HTML_content.append("<tr><th>Nodes under high resource usage:</th></tr>")
            HTML_content.append("<tr><th>Node</th><th>arch_string</th><th>swap_used</th><th>num_proc</th><th>swap_total</th><th>m_core</th><th>mem_used</th><th>m_socket</th><th>mem_total</th><th>np_load_avg</th></tr>")
            for node in input_data:
                HTML_content.append("<tr><td>")
                HTML_content.append(node)
                HTML_content.append("</td><td>")
                HTML_content.append(input_data[node]['arch_string'])
                HTML_content.append("</td><td>")
                HTML_content.append(input_data[node]['swap_used'])
                HTML_content.append("</td><td>")
                HTML_content.append(input_data[node]['num_proc'])
                HTML_content.append("</td><td>")
                HTML_content.append(input_data[node]['swap_total'])
                HTML_content.append("</td><td>")
                HTML_content.append(input_data[node]['m_core'])
                HTML_content.append("</td><td>")
                HTML_content.append(input_data[node]['mem_used'])
                HTML_content.append("</td><td>")
                HTML_content.append(input_data[node]['m_socket'])
                HTML_content.append("</td><td>")
                HTML_content.append(input_data[node]['mem_total'])
                HTML_content.append("</td><td>")
                HTML_content.append(input_data[node]['np_load_avg'])
                HTML_content.append("</td></tr>")
        elif write_code == 'ooc':
            HTML_content.append("<tr><th>Nodes under high resource usage:</th></tr>")
            HTML_content.append("<tr><th>Node</th><th>arch_string</th><th>swap_used</th><th>num_proc</th><th>swap_total</th><th>m_core</th><th>mem_used</th><th>m_socket</th><th>mem_total</th><th>np_load_avg</th></tr>")
            for node in input_data:
                HTML_content.append("<tr><td>")
                HTML_content.append(node)
                HTML_content.append("</td><td>")
                HTML_content.append(input_data[node]['arch_string'])
                HTML_content.append("</td><td>")
                HTML_content.append(input_data[node]['swap_used'])
                HTML_content.append("</td><td>")
                HTML_content.append(input_data[node]['num_proc'])
                HTML_content.append("</td><td>")
                HTML_content.append(input_data[node]['swap_total'])
                HTML_content.append("</td><td>")
                HTML_content.append(input_data[node]['m_core'])
                HTML_content.append("</td><td>")
                HTML_content.append(input_data[node]['mem_used'])
                HTML_content.append("</td><td>")
                HTML_content.append(input_data[node]['m_socket'])
                HTML_content.append("</td><td>")
                HTML_content.append(input_data[node]['mem_total'])
                HTML_content.append("</td><td>")
                HTML_content.append(input_data[node]['np_load_avg'])
                HTML_content.append("</td></tr>")
        else:
            pass

    HTML_structure = [
    "<table width=\"100%\">",
    "<tr><th>",
    "Date and time of update: ",
    "</th><th>",
    datetimenow,
    "</th></tr>",
    '\n'.join(HTML_content),
    "<tr><td></td></tr>",
    "</table>"
    ]

    # print('\n'.join(HTML_structure))

    with open(writeout_html, 'w') as writeout_fp:
        writeout_fp.write('\n'.join(HTML_structure))

    return True
