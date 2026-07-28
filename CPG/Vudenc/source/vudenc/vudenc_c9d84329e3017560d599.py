def run(self):...
"""docstring"""
while True:
self.update_log_filenames()
self.check_log_files_and_push_updates()
time.sleep(1)
