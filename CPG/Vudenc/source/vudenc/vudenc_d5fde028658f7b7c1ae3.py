def change_import_path(directory, module, src_file, dry_run=False):...
"""docstring"""
new_lines = []
module_present = False
current_file = os.path.join(directory, src_file)
if dry_run:
containt = file_to_read.read()
for line in file_to_read:
if module in containt:
if module in line:
if module_present:
if re.search('^import .*models.*|import .*models.*', containt):
module_present = True
new_lines.append(line)
for line in new_lines:
print("sed -i 's/([^ ]+)\\.{0}([^ \\n]+)/\\1\\2.{0}/g' {1}".format(module,
    src_file))
if re.search('^from .*models.*|from .*models.*', containt):
if 'from' not in line:
file_to_write.write(line)
print("sed -i 's/([^ ]+)\\.{0} import (\\w+)/\\1.\\2 import {0}/g' {1}".
    format(module, src_file))
new_lines.append(re.sub('(?P<pre>[^ ]+)\\.{}(?P<post>[^ \\n]+)'.format(
    module), '\\g<pre>\\g<post>.{}'.format(module), line))
new_lines.append(re.sub('(?P<pre>[^ ]+)\\.{} import (?P<post>\\w+)'.format(
    module), '\\g<pre>.\\g<post> import {}'.format(module), line))
