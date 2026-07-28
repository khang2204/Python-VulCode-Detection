def then_response_should_be_a_redirect_to(self, url):...
assert self.response.status_code == 302
assert self.response['Location'] == url
return self
