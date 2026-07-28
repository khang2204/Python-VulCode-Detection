def yield_swarming_bot_files(root_dir, host, host_version, additionals):...
"""docstring"""
items = {i: None for i in FILES}
items.update(additionals)
config = {'server': host.rstrip('/'), 'server_version': host_version}
items['config/config.json'] = json.dumps(config)
for item, content in sorted(items.iteritems()):
if content is not None:
yield item, content
yield item, f.read()
