def test_success(self):...
if self.status_code not in [200, 302]:
return False
if self.status_code == 200 and self.res_data is None:
return False
if self.status_code == 200 and len(self.res_data
return False
return True
