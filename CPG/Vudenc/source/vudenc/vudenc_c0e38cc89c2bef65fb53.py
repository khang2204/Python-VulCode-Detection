def command(**kwargs) ->typing.Callable[[typing.Any], commands.Command]:...
"""docstring"""
kwargs.setdefault('cls', NekoCommand)
return commands.command(**kwargs)
