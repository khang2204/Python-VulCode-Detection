def __init__(self, yaml_config, header):...
self.icinga_lines = []
self.indent = CONFIG['INDENT']
self.icinga_lines.extend(header.serialize())
self.write_section('host', yaml_config.host)
for service in yaml_config.services:
self.write_section('service', service)
