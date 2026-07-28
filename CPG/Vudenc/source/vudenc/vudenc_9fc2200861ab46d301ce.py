def mirror(self, dst_dir):...
source_dir = self.directory
def mkdir_p(path):...
if path.strip() != '' and not os.path.exists(path):
os.makedirs(path)
env = os.environ.copy()
env['LC_MESSAGES'] = 'C'
def tracked_files():...
p = Popen(['git', 'ls-tree', '-r', '--name-only', 'HEAD'], stdout=PIPE, env=env
    )
out = p.communicate()[0]
if p.returncode != 0 or not out.strip():
return None
return [e.strip() for e in out.splitlines() if os.path.exists(e)]
