import os
from core.colors import *
from files.config import *
from core.verbout import verbout
from files.discovered import INTERNAL_URLS, FILES_EXEC, SCAN_ERRORS
from files.discovered import VULN_LIST, FORMS_TESTED, REQUEST_TOKENS
def logger(filename, content):...
"""docstring"""
output_file = OUTPUT_DIR + filename + '.log'
if type(content) is tuple or type(content) is list:
for m in content:
f.write(content)
f.write(m + '\n')
f.write('\n')
def pheaders(tup):...
"""docstring"""
verbout(GR, 'Receiving headers...\n')
verbout(color.GREY, '  ' + color.UNDERLINE + 'HEADERS' + color.END + color.
    GREY + ':' + '\n')
for key, val in tup.items():
verbout('  ', color.CYAN + key + ': ' + color.ORANGE + val)
verbout('', '')
def GetLogger():...
if INTERNAL_URLS:
logger('internal-links', INTERNAL_URLS)
if SCAN_ERRORS:
logger('errored', SCAN_ERRORS)
if FILES_EXEC:
logger('files-found', FILES_EXEC)
if REQUEST_TOKENS:
logger('anti-csrf-tokens', REQUEST_TOKENS)
if FORMS_TESTED:
logger('forms-tested', FORMS_TESTED)
if VULN_LIST:
logger('vulnerabilities', VULN_LIST)
def ErrorLogger(url, error):...
con = '(i) ' + url + ' -> ' + error.__str__()
SCAN_ERRORS.append(con)
def VulnLogger(url, vuln):...
tent = '[!] ' + url + ' -> ' + vuln
VULN_LIST.append(tent)
