def encrypt_password(password, key=None):...
if key is None:
p_key = PASSWORD_KEY
p_key = key
bin_password = password.encode('utf-8')
bin_salt = p_key.encode('utf-8')
m = hashlib.sha256()
for n in range(1, 1000):
m.update(bin_password + bin_salt)
m = m.digest()
encrypted_password = base64.b64encode(m)
return encrypted_password
