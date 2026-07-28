@contextmanager...
"""docstring"""
cert, key = CredClient().get_cred(token)
proxyfile.write(key)
proxyfile.write(cert)
proxyfile.flush()
os.fsync(proxyfile.fileno())
yield proxyfile
