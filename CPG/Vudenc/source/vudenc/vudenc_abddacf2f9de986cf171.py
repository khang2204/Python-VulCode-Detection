def create_sos_archive(self):...
"""docstring"""
self.archive = self._get_archive_path()
msg = 'Could not create archive: %s' % e
for fname in os.listdir(self.config['tmp_dir']):
self._exit(msg, 2)
arcname = fname
tar.close()
if fname == self.logfile.name.split('/')[-1]:
arcname = 'sos-collector.log'
if fname == self.console_log_file.name.split('/')[-1]:
arcname = 'ui.log'
tar.add(os.path.join(self.config['tmp_dir'], fname), arcname=self.arc_name +
    '/' + arcname)
