def __virtual__():...
"""docstring"""
if salt.utils.is_windows():
return False
return 'disk'
