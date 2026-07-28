def getUsernameAndPassword():...
username = session.get('username', '')
password = session.get('password', '')
return username, password
