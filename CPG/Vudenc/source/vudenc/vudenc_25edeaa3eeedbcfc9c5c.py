def delete_WifiConn(wifiap):...
"""docstring"""
ps = subprocess.Popen(['nmcli', 'connection', 'delete', 'id', wifiap],
    stdout=subprocess.PIPE)
print(ps)
