def open_ssh_client():...
"""docstring"""
username, hostname = get_connection_tuple(CONNECTION_STRING)
client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(username=username, password=SERVER_PASSWORD, hostname=hostname)
return client
