def ansi(keyword):...
codes = {'bluef': '\x1b[34m', 'boldon': '\x1b[1m', 'boldoff': '\x1b[22m',
    'redf': '\x1b[31m', 'reset': '\x1b[0m', 'yellowf': '\x1b[33m'}
if keyword in codes:
return codes[keyword]
return ''
