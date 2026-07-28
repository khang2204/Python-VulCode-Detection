def tpl(*args, **ka):...
"""docstring"""
tp = MetalTemplate('\n' + args[0], tags=ka)
x = tp.render(ka)
return x[1:]
