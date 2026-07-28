@handle_html...
session = await get_session(request)
data = await request.post()
uname = session['uname']
if 'action' in data:
if data['action'] == 'change_password':
return f'Invalid POST request: <i>{data.items()}</i>'
if set(['cpsw', 'psw', 'psw2']).issubset(data.keys()):
if data['psw'] != data['psw2']:
return "New passwords doesn't match!"
entry = await database.select_user(request, uname)
if not entry:
return 'Error: Logged in as non-existing user! (what?)'
cpsw = data['cpsw']
if bcrypt.hashpw(cpsw.encode('UTF-8'), entry[0][2].encode('UTF-8')).decode(
return 'Error: "Current password" was incorrect'
psw = data['psw']
bhash = bcrypt.hashpw(psw.encode('UTF-8'), bcrypt.gensalt()).decode('UTF-8')
await database.update_user_password(request, uname, bhash)
return """Success! Your password has been changed!<br>
<a href="/settings">Click here to go back.</a>"""
