def executable_exists(executable):...
"""docstring"""
for directory in os.getenv('PATH').split(':'):
if os.path.exists(os.path.join(directory, executable)):
return False
return True
