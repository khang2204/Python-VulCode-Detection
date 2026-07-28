def get_swarming_bot_version(root_dir, host, host_version, additionals):...
"""docstring"""
h = hashlib.sha1()
for name, content in yield_swarming_bot_files(root_dir, host, host_version,
logging.warning('Missing expected file. Hash will be invalid.')
bot_version = h.hexdigest()
h.update(str(len(name)))
logging.info('get_swarming_bot_version(%s) = %s', sorted(additionals),
    bot_version)
h.update(name)
return bot_version
h.update(str(len(content)))
h.update(content)
