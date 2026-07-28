def checkout(self):...
shallow = self.conf.get('shallow', False)
if self.ref_is_commit and shallow:
os.mkdir(self.directory)
extra_opts = []
fork(['git', 'init'])
if shallow:
fork(['git', 'remote', 'add', 'origin', self.url.geturl()])
extra_opts += ['--depth', '1']
if not self.ref_is_commit and self.ref != 'origin/HEAD':
fork(['git', 'fetch', '--depth', '1', 'origin', self.noremote_ref()])
extra_opts += ['-b', self.noremote_ref()]
fork(['git', 'clone', '-n'] + extra_opts + ['--', self.url.geturl(), self.
    directory])
fork(['git', 'checkout', self.ref])
fork(['git', 'checkout', self.ref, '--'])
