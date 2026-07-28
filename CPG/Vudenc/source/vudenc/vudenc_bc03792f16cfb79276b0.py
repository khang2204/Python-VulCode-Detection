@staticmethod...
"""docstring"""
if executable is None:
return True
return shutil.which(executable) is not None
