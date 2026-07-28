def render_POST(self, request):...
"""docstring"""
dmode = request.args.get('mode', [None])[0]
if dmode == 'init':
return self.mode_init(request)
if dmode == 'input':
return self.mode_input(request)
if dmode == 'receive':
return self.mode_receive(request)
if dmode == 'close':
return self.mode_close(request)
if dmode == 'keepalive':
return self.mode_keepalive(request)
return '""'
