def create_basename(input_string, blog):...
"""docstring"""
if not input_string:
input_string = 'page'
basename = input_string
basename_test = create_basename_core(basename)
from core.models import Page
n = 0
while True:
Page.get(Page.basename == basename_test, Page.blog == blog)
return basename_test[:MAX_BASENAME_LENGTH]
n += 1
basename_test = basename + '-' + str(n)
