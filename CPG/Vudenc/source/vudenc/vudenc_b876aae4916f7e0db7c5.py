def run(self, headers):...
response = super(HttpHead, self).run(headers)
self.logger.print_response_code(response)
self.logger.print_headers(headers.items(), sending=True)
self.logger.print_headers(response.getheaders())
