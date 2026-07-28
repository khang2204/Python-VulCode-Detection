def include(self, snakefile, overwrite_first_rule=False, print_compilation=...
"""docstring"""
if not urllib.parse.urlparse(snakefile).scheme:
if not os.path.isabs(snakefile) and self.included_stack:
if snakefile in self.included:
current_path = os.path.dirname(self.included_stack[-1])
snakefile = os.path.abspath(snakefile)
logger.info('Multiple include of {} ignored'.format(snakefile))
self.included.append(snakefile)
snakefile = os.path.join(current_path, snakefile)
return
self.included_stack.append(snakefile)
workflow = self
first_rule = self.first_rule
code, linemap = parse(snakefile, overwrite_shellcmd=self.overwrite_shellcmd)
if print_compilation:
print(code)
sys.path.insert(0, os.path.dirname(snakefile))
self.linemaps[snakefile] = linemap
exec(compile(code, snakefile, 'exec'), self.globals)
if not overwrite_first_rule:
self.first_rule = first_rule
self.included_stack.pop()
