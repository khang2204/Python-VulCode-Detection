def add_newWifiConn(wifiname, wifipass):...
print(wlans)
wlan0 = wlans[0]
print(wlan0)
print(wifiname)
for dev in wlans:
for ap in dev.AccessPoints:
print(currentwifi)
if ap.Ssid == wifiname:
params = {'802-11-wireless': {'security': '802-11-wireless-security'},
    '802-11-wireless-security': {'key-mgmt': 'wpa-psk', 'psk': wifipass}}
currentwifi = ap
conn = nm.AddAndActivateConnection(params, wlan0, currentwifi)
