def has_token():...
if request.params.get('_csrftoken', None) in session['modtokens']:
tokens = session['modtokens']
return False
tokens.remove(request.params.get('_csrftoken'))
session['modtokens'] = tokens
session.save()
return True
