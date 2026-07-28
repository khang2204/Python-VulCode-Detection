def get_allconfiguredwifi():...
"""docstring"""
ps = subprocess.Popen('nmcli -t -f NAME,TYPE conn | grep 802-11-wireless',
    shell=True, stdout=subprocess.PIPE).communicate()[0]
wifirows = ps.split('\n')
wifi = []
for row in wifirows:
name = row.split(':')
return wifi
print(name)
wifi.append(name[0])
