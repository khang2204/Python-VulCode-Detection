def packJWT(data, sign_key, encrypt_key):...
"""docstring"""
token = jwt.encode(data, sign_key, algorithm='RS256')
enc_token = HybridRSA.encrypt(token, encrypt_key)
return b64encode(enc_token).decode('utf-8')
