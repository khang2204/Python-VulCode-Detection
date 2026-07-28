def check_registered_by_address(address):...
address = address.split('_')[1]
mycursor.execute("SELECT username FROM accounts WHERE address='%s'" % (
    'xrb_' + address))
result = mycursor.fetchall()
if len(result) > 0:
return result[0][0]
mycursor.execute("SELECT username FROM accounts WHERE address='%s'" % (
    'nano_' + address))
result = mycursor.fetchall()
if len(result) > 0:
return result[0][0]
return None
