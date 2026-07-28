def get_customer_id(query):...
print('username: ', end='')
username = input()
while len(username) == 0:
print("""username must exceed zero characters.
username: """, end='')
return username_to_id(username, query)
username = input()
