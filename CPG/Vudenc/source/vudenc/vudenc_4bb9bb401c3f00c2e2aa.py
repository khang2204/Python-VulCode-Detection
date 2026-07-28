def edit_WifiConn(wifiname, wifipass):...
ps = subprocess.Popen(['nmcli', 'connection', 'delete', 'id', wifiname],
    stdout=subprocess.PIPE)
print(ps)
print(wlans)
wlan0 = wlans[0]
print(wlan0)
print(wifiname)
for dev in wlans:
for ap in dev.AccessPoints:
params = {'802-11-wireless': {'security': '802-11-wireless-security'},
    '802-11-wireless-security': {'key-mgmt': 'wpa-psk', 'psk': wifipass}}
if ap.Ssid == wifiname:
conn = nm.AddAndActivateConnection(params, wlan0, currentwifi)
currentwifi = ap
return
