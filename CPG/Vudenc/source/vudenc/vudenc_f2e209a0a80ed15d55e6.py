def IO_redirection(cmd):...
"""docstring"""
if '<' in cmd:
SetUpInputRedirect(cmd)
if '>' in cmd:
SetUpOutputRedirect(cmd)
if '>>' in cmd:
SetUpAppendRedirect(cmd)
