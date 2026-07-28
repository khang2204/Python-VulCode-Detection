def pheaders(tup):...
"""docstring"""
verbout(GR, 'Receiving headers...\n')
verbout(color.GREY, '  ' + color.UNDERLINE + 'HEADERS' + color.END + color.
    GREY + ':' + '\n')
for key, val in tup.items():
verbout('  ', color.CYAN + key + ': ' + color.ORANGE + val)
verbout('', '')
