def device_for_ide_port(self, port_id):...
"""docstring"""
if port_id > 3:
return None
g0 = '00000000'
if port_id > 1:
g0 = '00000001'
err, output = shellutil.run_get_output(
    'sysctl dev.storvsc | grep pnpinfo | grep deviceid=')
port_id = port_id - 2
if err:
return None
g1 = '000' + ustr(port_id)
g0g1 = '{0}-{1}'.format(g0, g1)
"""
        search 'X' from 'dev.storvsc.X.%pnpinfo: classid=32412632-86cb-44a2-9b5c-50d1417354f5 deviceid=00000000-0001-8899-0000-000000000000'
        """
cmd_search_ide = ('sysctl dev.storvsc | grep pnpinfo | grep deviceid={0}'.
    format(g0g1))
err, output = shellutil.run_get_output(cmd_search_ide)
if err:
return None
cmd_extract_id = cmd_search_ide + "|awk -F . '{print $3}'"
err, output = shellutil.run_get_output(cmd_extract_id)
"""
        try to search 'blkvscX' and 'storvscX' to find device name
        """
output = output.rstrip()
cmd_search_blkvsc = (
    "camcontrol devlist -b | grep blkvsc{0} | awk '{{print $1}}'".format(
    output))
err, output = shellutil.run_get_output(cmd_search_blkvsc)
if err == 0:
output = output.rstrip()
cmd_search_storvsc = (
    "camcontrol devlist -b | grep storvsc{0} | awk '{{print $1}}'".format(
    output))
cmd_search_dev = (
    "camcontrol devlist | grep {0} | awk -F \\( '{{print $2}}'|sed -e 's/.*(//'| sed -e 's/).*//'"
    .format(output))
err, output = shellutil.run_get_output(cmd_search_storvsc)
err, output = shellutil.run_get_output(cmd_search_dev)
if err == 0:
if err == 0:
output = output.rstrip()
return None
for possible in output.rstrip().split(','):
cmd_search_dev = (
    "camcontrol devlist | grep {0} | awk -F \\( '{{print $2}}'|sed -e 's/.*(//'| sed -e 's/).*//'"
    .format(output))
if not possible.startswith('pass'):
err, output = shellutil.run_get_output(cmd_search_dev)
return possible
if err == 0:
for possible in output.rstrip().split(','):
if not possible.startswith('pass'):
return possible
