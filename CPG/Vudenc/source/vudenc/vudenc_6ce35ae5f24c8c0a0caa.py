def pipe(self, command, data):...
p = subprocess.Popen(command, shell=True, bufsize=-1, stdout=subprocess.
    PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
output, error = p.communicate(data)
result = None
if error:
self.logger.print_error(error.decode('utf-8'))
result = output.decode('utf-8')
return result
