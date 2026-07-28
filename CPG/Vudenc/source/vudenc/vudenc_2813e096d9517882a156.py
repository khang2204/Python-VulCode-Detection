@staticmethod...
"""docstring"""
iface = ''
inet = ''
mac = ''
err, output = shellutil.run_get_output('ifconfig -l ether', chk_err=False)
if err:
ifaces = output.split()
if not ifaces:
iface = ifaces[0]
err, output = shellutil.run_get_output('ifconfig ' + iface, chk_err=False)
if err:
for line in output.split('\n'):
if line.find('inet ') != -1:
logger.verbose('Interface info: ({0},{1},{2})', iface, inet, mac)
inet = line.split()[1]
if line.find('ether ') != -1:
return iface, inet, mac
mac = line.split()[1]
