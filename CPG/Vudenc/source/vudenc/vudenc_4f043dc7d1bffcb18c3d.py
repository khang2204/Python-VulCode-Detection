def logger(filename, content):...
"""docstring"""
output_file = OUTPUT_DIR + filename + '.log'
if type(content) is tuple or type(content) is list:
for m in content:
f.write(content)
f.write(m + '\n')
f.write('\n')
