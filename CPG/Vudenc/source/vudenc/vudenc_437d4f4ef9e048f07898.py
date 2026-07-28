def test_success(self):...
if not GenericRequest.test_success(self):
return False
username_re = re.compile(self.username)
if self.loggedin:
if username_re.search(self.res_data) is None:
if username_re.search(self.res_data) is not None:
return False
return True
return False
