def mirror(self, dst, quick=False):...
import shutil
src = self.directory
os.chdir(src)
if not quick and isdir(dst):
shutil.rmtree(dst)
if not isdir(dst):
os.makedirs(dst)
env = os.environ.copy()
env['LC_MESSAGES'] = 'C'
dirs = ['.']
for D in dirs:
infos = {}
for L in Popen(['svn', 'info', '--recursive', D], stdout=PIPE, env=env).stdout:
L = L.decode()
if L.strip():
k, v = L.strip().split(': ', 1)
if infos['Schedule'] == 'delete':
infos[k] = v
fn = infos['Path']
infos = {}
if fn == '.':
fn1 = join(src, fn)
fn2 = join(dst, fn)
if isdir(fn1):
if not isdir(fn2):
if not quick or newer(fn1, fn2):
os.makedirs(fn2)
shutil.copy2(fn1, fn2)
