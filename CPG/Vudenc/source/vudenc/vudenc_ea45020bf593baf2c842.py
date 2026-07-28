def csrf_hash(csrf):...
"""docstring"""
enc = str(csrf) + SECRET_KEY
m = hashlib.sha256()
m.update(enc.encode('utf-8'))
m = m.digest()
encrypted_csrf = base64.b64encode(m).decode('utf-8')
return encrypted_csrf
