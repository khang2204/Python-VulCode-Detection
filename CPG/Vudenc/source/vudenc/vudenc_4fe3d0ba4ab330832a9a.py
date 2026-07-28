def multiple_hash_password(password, salt):...
hash_value = password + salt
for _ in range(1000):
hash_value = hashlib.sha3_512((hash_value + password + salt).encode()
    ).hexdigest()
return hash_value
