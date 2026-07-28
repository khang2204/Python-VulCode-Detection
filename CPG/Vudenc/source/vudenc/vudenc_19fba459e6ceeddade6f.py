def log_zinc_file(self, analysis_file):...
self.context.log.debug('Calling zinc on: {} ({})'.format(analysis_file, 
    hash_file(analysis_file).upper() if os.path.exists(analysis_file) else
    'nonexistent'))
