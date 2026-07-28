import sys
import os
import re
import json
import shlex
import urllib.request
import codecs
reader = codecs.getreader('utf-8')
return_code = 0
HEADER = '\x1b[94m'
OKBLUE = '\x1b[94m'
OKGREEN = '\x1b[92m'
WARNING = '\x1b[93m'
MAYBE_FAIL = '\x1b[96m'
FAIL = '\x1b[91m'
END = '\x1b[0m'
BOLD = '\x1b[1m'
UNDERLINE = '\x1b[4m'
def header(app):...
print(
    """
    [{header}{bold}YunoHost App Package Linter{end}]

 App packaging documentation - https://yunohost.org/#/packaging_apps
 App package example         - https://github.com/YunoHost/example_ynh
 Official helpers            - https://yunohost.org/#/packaging_apps_helpers_en
 Experimental helpers        - https://github.com/YunoHost-Apps/Experimental_helpers

    Analyzing package {header}{app}{end}"""
    .format(header=c.HEADER, bold=c.BOLD, end=c.END, app=app))
def print_header(str):...
print('\n [' + c.BOLD + c.HEADER + str.title() + c.END + ']\n')
def print_right(str):...
print(c.OKGREEN + '✔', str, c.END)
def print_warning(str):...
print(c.WARNING + '!', str, c.END)
def print_error(str, reliable=True):...
if reliable:
return_code = 1
print(c.MAYBE_FAIL + '?', str, c.END)
print(c.FAIL + '✘', str, c.END)
def urlopen(url):...
conn = urllib.request.urlopen(url)
return {'content': '', 'code': e.code}
return {'content': conn.read().decode('UTF8'), 'code': 200}
