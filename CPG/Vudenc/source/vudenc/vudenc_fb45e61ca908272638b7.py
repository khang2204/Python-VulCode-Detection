@handle_html...
session = await get_session(request)
data = await request.post()
if set(['action', 'uname', 'psw']).issubset(data.keys()
uname = data['uname']
if 'action' in data:
psw = data['psw']
if data['action'] == 'logout' and 'uname' in session:
return f"""Invalid login POST:<br/><i>{data.items()}</i><br>
Already logged in: {'uname' in session}"""
if data['action'] == 'login':
for i in ('uname', 'ignore_timeout'):
entry = await database.select_user(request, uname)
if data['action'] == 'register' and 'psw2' in data:
if i in session:
return 'Logged out'
if not entry:
if not is_valid_username(uname):
return 'Error: No such user.'
if bcrypt.hashpw(psw.encode('UTF-8'), entry[0][2].encode('UTF-8')).decode(
return f"""Error: invalid username: <i>{uname}</i><br>
We only allow characters from the english alphabet plus digits"""
if psw != data['psw2']:
return 'Error: Wrong password'
session['uname'] = uname
return 'Error: mismatching passwords!'
bhash = bcrypt.hashpw(psw.encode('UTF-8'), bcrypt.gensalt()).decode('UTF-8')
session['login_time'] = time.time()
await database.insert_user(request, uname, bhash)
return 'Error: username already taken!'
return 'User created! <a href="/login">login over here.</a>'
if 'keep' in data and data['keep'] == 'logged_in':
session['ignore_timeout'] = True
out = 'Login successfull!'
if 'return_after_login' in session:
out += f"""<br/>
<a href="{session['return_after_login']}">Go back</a>"""
return out
