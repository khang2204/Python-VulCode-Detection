import json
import os
import pathlib
import re
import shlex
import subprocess
import sys
from collections import OrderedDict
from operator import itemgetter
import click
CONFIG = {'syscall_header_file': '/usr/include/bits/syscall.h',
    'cache_file_32bit': '{}/.cache/syscall_number/32bit.json'.format(os.
    environ['HOME']), 'cache_file_64bit':
    '{}/.cache/syscall_number/64bit.json'.format(os.environ['HOME'])}
BITNESS_32 = '32'
BITNESS_64 = '64'
def read_file_content(file_path):...
return pathlib.Path(file_path).read_text()
def write_file_content(file_path, data):...
return pathlib.Path(file_path).write_text(data)
def parse_syscall_names():...
syscall_names = []
syscall_name_regex = re.compile('^.+SYS_(?P<syscall_name>[^ ]+)')
content = read_file_content(CONFIG['syscall_header_file'])
for line in content.split('\n'):
match = syscall_name_regex.match(line)
return syscall_names
if match:
syscall_names.append(match.group('syscall_name'))
