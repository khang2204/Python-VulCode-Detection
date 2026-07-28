def test_success(self):...
if not GenericRequest.test_success(self):
return False
return self.get_user_test_id() is not None
