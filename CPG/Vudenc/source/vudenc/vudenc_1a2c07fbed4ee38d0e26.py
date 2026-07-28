def handle_html(func):...
async def ret(*args, **kwargs):...
session = await get_session(args[0])
if 'uname' in session and 'ignore_timeout' not in session:
t = time.time()
session['visit_time'] = time.time()
prev = session['visit_time']
text = await func(*args, **kwargs)
if t - prev > handle_html.timeout:
out = web.Response(content_type='text/html', text=HTML_base.format(text=text))
session['visit_time'] = t
return out
