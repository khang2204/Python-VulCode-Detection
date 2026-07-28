def group(**kwargs) ->typing.Callable[[typing.Any], commands.Group]:...
"""docstring"""
kwargs.setdefault('cls', NekoGroup)
return commands.command(**kwargs)
