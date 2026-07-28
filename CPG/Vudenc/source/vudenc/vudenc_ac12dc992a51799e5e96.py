@handle_html...
session = await get_session(request)
if 'uname' not in session:
return base
return """<b>You're already logged in as <i>%s</i>!</b>
<form action='/login' method='post'><input type='submit' name='action' value='logout'/></form>""" % session[
    'uname']
