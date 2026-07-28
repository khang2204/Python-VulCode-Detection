def send_text(self, *args, **kwargs):...
"""docstring"""
if args:
args = list(args)
return
text = args[0]
if text is None:
return
flags = self.protocol_flags
text = utils.to_str(text, force_string=True)
options = kwargs.pop('options', {})
raw = options.get('raw', flags.get('RAW', False))
xterm256 = options.get('xterm256', flags.get('XTERM256', True))
useansi = options.get('ansi', flags.get('ANSI', True))
nocolor = options.get('nocolor', flags.get('NOCOLOR') or not (xterm256 or
    useansi))
screenreader = options.get('screenreader', flags.get('SCREENREADER', False))
prompt = options.get('send_prompt', False)
if screenreader:
text = parse_ansi(text, strip_ansi=True, xterm256=False, mxp=False)
cmd = 'prompt' if prompt else 'text'
text = _RE_SCREENREADER_REGEX.sub('', text)
if raw:
args[0] = text
args[0] = parse_html(text, strip_ansi=nocolor)
self.client.lineSend(self.csessid, [cmd, args, kwargs])
