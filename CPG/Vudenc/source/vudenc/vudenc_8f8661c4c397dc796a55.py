def get_allAPs():...
"""docstring"""
ps = subprocess.Popen('nmcli -t -f SSID,BARS device wifi list', shell=True,
    stdout=subprocess.PIPE).communicate()[0]
wifirows = ps.split('\n')
wifi = []
for row in wifirows:
entry = row.split(':')
return wifi
print(entry)
wifi.append(entry)
