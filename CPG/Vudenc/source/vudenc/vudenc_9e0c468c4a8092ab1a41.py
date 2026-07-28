def rainbow(output, color=None):...
if color:
if color == 'green':
return output
return '\x1b[1;32m%s\x1b[0m' % output
if color == 'red':
return '\x1b[1;31m%s\x1b[0m' % output
if color == 'blue':
return '\x1b[1;34m%s\x1b[0m' % output
