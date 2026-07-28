def start_server(self, verbose=False):...
self.install_prerequisites()
self.port = find_free_port()
if verbose:
stdout = None
stdout = subprocess.PIPE
stderr = None
stderr = subprocess.PIPE
env = os.environ.copy()
env['LANGUAGE'] = 'en'
h, self.tmp_db = tempfile.mkstemp(prefix='local_gae')
os.close(h)
cmd = [sys.executable, os.path.join(GAE_SDK, 'dev_appserver.py'), self.
    base_dir, '--port', str(self.port), '--datastore_path', self.tmp_db,
    '--datastore_consistency_policy', 'consistent', '--skip_sdk_update_check']
if verbose:
cmd.extend(['--log_level', 'debug'])
self.test_server = subprocess.Popen(cmd, stdout=stdout, stderr=stderr, env=env)
while not test_port(self.port):
self.test_server.poll()
self.url = 'http://localhost:%d/' % self.port
if self.test_server.returncode is not None:
time.sleep(0.001)
