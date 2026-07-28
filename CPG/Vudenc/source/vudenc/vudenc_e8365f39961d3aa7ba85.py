def parse_line(self, line):...
"""docstring"""
cmd_name, cmd_args = line.partition(' ')[::2]
command_cls = cmd.get_command(cmd_name)
tokenized_cmd_args = self.tokenizer.tokenize(cmd_args.strip())
return command_cls(self), tokenized_cmd_args
