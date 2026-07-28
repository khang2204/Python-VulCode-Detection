def accept_license_terms(self, license_id: int):...
"""docstring"""
image_license = License.get_by_id(license_id)
self.accepted_licenses.append(image_license)
db.session.commit()
