def _query_arg(self, argument_name, output=None, default=None):...
"""docstring"""
arg = self.r_handler.get_query_argument(argument_name, None)
if not arg:
return default
if output is bool:
return arg.lower() == 'true'
if output is list:
return arg.split(',')
if output is not None:
return output(arg)
return arg
