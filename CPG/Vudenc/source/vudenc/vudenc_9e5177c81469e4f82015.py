def run(self, headers):...
response = super(HttpGet, self).run(headers)
self.logger.print_response_code(response)
self.logger.print_headers(response.getheaders())
data = response.read()
if self.pipe_command:
data = self.pipe(self.pip_command, data)
if data:
self.logger.print_data(data)
