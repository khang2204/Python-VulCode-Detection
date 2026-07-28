def loadClientRSAKey(client):...
"""docstring"""
key = open('keys/%s/key_rsa.pub' % client, 'rb').read()
return key
