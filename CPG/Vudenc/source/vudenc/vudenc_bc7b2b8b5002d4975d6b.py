def make_token():...
tokens = session.get('modtokens', [])
token = None
if len(tokens) < 100:
token = hashlib.sha1(str(random.random())).hexdigest()
token = tokens[-1]
tokens.append(token)
session['modtokens'] = tokens
session.save()
return token
