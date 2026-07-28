def generate_csrf_token():...
if '_csrf_token' not in session:
session['_csrf_token'] = ''.join(random.choice(string.ascii_uppercase +
    string.digits) for x in range(16))
return session['_csrf_token']
