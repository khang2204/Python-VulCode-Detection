def test_success(self):...
if not LoginRequest.test_success(self):
return False
if self.redirected_to != self.base_url:
return False
return True
