def run(self, handler):
        params = handler.params

        if handler.risk < 3:
            content = self.warning.format(handler.risk)
        else:
            content = 'Try <a href="{}">this</a> or <a href="{}">this</a>...'.format(self.good_path, self.evil_path)
            if 'domain' in params:
                command = 'host' if os.name != 'nt' else 'nslookup'
                domain = params.get('domain', '/')[0]
                output = subprocess.check_output(
                    ' '.join([command, domain]),
                    shell=True,
                    stderr=subprocess.STDOUT,
                    stdin=subprocess.PIPE
                )
                content = '<pre>{}</pre>'.format(output.decode())

        return content


class UnsafeDeserialization(Attack):

    class RCE:
        def __reduce__(self):
            cmd = ('whoami >> poc.txt')
