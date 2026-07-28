def grid(dims, files, implicitFillWidth=True):...
x = 0
y = len(files)
for line in files:
if len(line) > x:
dims = (dims[0][0] / x, dims[0][1]) if dims[0] else None, (dims[1][0] / y,
    dims[1][1]) if dims[1] else None
x = len(line)
if not (dims[0] or dims[1]):
if implicitFillWidth:
s = ''
dims = (1.0 / x, '\\textwidth'), None
dims = None, (1.0 / y, '\\textheight')
for line in files:
for file in line:
return s
s += singleImage(dims, file=file)
s += '\\\\'
