import sys
import os
import contextlib
def IO_redirection(cmd):...
"""docstring"""
if '<' in cmd:
SetUpInputRedirect(cmd)
if '>' in cmd:
SetUpOutputRedirect(cmd)
if '>>' in cmd:
SetUpAppendRedirect(cmd)
def SetUpInputRedirect(cmd):...
import pdb
pdb.set_trace()
def SetUpOutputRedirect(cmd):...
i = cmd.index('>')
sys.stdout = open(cmd[i + 1], 'w')
print('this is a test')
def SetUpAppendRedirect(cmd):...
import pdb
pdb.set_trace()
