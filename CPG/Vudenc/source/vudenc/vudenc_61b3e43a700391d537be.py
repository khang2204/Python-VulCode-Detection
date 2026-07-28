def has_user_accepted_licence(self, license_id: int):...
"""docstring"""
image_license = License.get_by_id(license_id)
if image_license in self.accepted_licenses:
return True
return False
