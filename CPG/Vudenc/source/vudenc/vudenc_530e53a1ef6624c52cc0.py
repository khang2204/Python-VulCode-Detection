def create_tmp_dir(self):...
"""docstring"""
tmpdir = tempfile.mkdtemp(prefix='sos-collector-', dir='/var/tmp')
self.config['tmp_dir'] = tmpdir
self.config['tmp_dir_created'] = True
