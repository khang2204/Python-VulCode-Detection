def get_swarming_bot_zip(root_dir, host, host_version, additionals):...
"""docstring"""
zip_memory_file = StringIO.StringIO()
h = hashlib.sha1()
for name, content in yield_swarming_bot_files(root_dir, host, host_version,
zip_file.writestr(name, content)
data = zip_memory_file.getvalue()
h.update(str(len(name)))
bot_version = h.hexdigest()
h.update(name)
logging.info('get_swarming_bot_zip(%s) is %d bytes; %s', additionals.keys(),
    len(data), bot_version)
h.update(str(len(content)))
return data, bot_version
h.update(content)
