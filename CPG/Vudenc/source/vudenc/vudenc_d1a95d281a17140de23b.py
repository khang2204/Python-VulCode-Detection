"""
raut2webstr-pagemodel-tree import-path script
"""
import argparse
import os
import sys
import re
RAUT_MODULES = 'models', 'pages'
def is_py_file(filename):...
return filename.endswith('.py') and filename != '__init__.py'
