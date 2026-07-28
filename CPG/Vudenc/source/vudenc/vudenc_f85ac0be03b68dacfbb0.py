def add_new_account(username):...
address = generate_account()
private = address['private']
address = address['account']
print(type(private), type(address), type(username))
print(private, address, username)
sql = (
    'INSERT INTO accounts (username, private_key, address, minimum) VALUES (%s, %s, %s, %s)'
    )
val = username, private, address, nano_to_raw(0.01)
mycursor.execute(sql, val)
mydb.commit()
return address
