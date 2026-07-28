def cleanup(self):...
"""docstring"""
self.remove_sos_archive()
if self.hash_retrieved:
self.remove_file(self.sos_path + '.md5')
cleanup = self.host.set_cleanup_cmd()
if cleanup:
self.run_command(cleanup)
