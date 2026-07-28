def write_output(self, file_name, yaml_icinga):...
lines = yaml_icinga.icinga_lines
output_writer = OutputWriter(self.output_path(file_name))
output_writer.write_lines(lines)
