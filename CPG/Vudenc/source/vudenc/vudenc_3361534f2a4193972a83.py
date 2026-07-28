def create_new_user(username, query):...
print('first name: ', end='')
fname = input()
print('last name: ', end='')
lname = input()
print('phone number (xxxxxxxxxxx): ', end='')
phone = input()
phone = int(phone) if phone.isdigit() else None
print('email: ', end='')
email = input()
print('street address: ', end='')
street = input()
print('city: ', end='')
city = input()
print('state: ', end='')
state = input()
print('zipcode: ', end='')
zip = input()
zip = int(zip) if zip.isdigit() else None
print('country: ', end='')
country = input()
query.cursor.execute('SELECT MAX(frequent_shopper_id) FROM customer;')
freq_shop_id = query.cursor.fetchone()[0] + 1
query.cursor.execute(
    'INSERT INTO customer (first_name, last_name, phone_number, username, email, frequent_shopper_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;'
    , (fname, lname, phone, username, email, freq_shop_id))
customer_id = query.cursor.fetchone()[0]
query.cursor.execute(
    'INSERT INTO address (address_line, zipcode, city, state, country) VALUES (%s, %s, %s, %s, %s) RETURNING id;'
    , (street, zip, city, state, country))
address_id = query.cursor.fetchone()[0]
query.cursor.execute(
    'INSERT INTO customer_to_address (customer_id, address_id) VALUES (%s, %s);'
    , (customer_id, address_id))
query.commit()
print('user ' + username + ' created ✓')
return freq_shop_id
