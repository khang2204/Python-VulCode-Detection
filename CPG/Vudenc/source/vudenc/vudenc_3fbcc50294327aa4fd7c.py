def generate(self):...
file_name = None
raw_yaml_config, header_source = read_config(self.source)
if raw_yaml_config is None:
yaml_config = YamlConfig(raw_yaml_config, skip_checks=self.skip_checks)
if yaml_config.host and self._is_newer(header_source, yaml_config.host_name):
file_name = self.create_filename(yaml_config.host_name)
if file_name:
yaml_icinga = YamlToIcinga(yaml_config, header_source)
LOG.info("Icinga config file '%s' created." % file_name)
return file_name
self.write_output(file_name, yaml_icinga)
