def init(self):...
"""docstring"""
self.require_user_role('user', self.params.cc)
self.version = utils.get_latest_version(self.params.cc)
self.facility = model.Facility.get_by_key_name(self.params.facility_name,
    self.version)
if not self.facility:
self.facility_type = model.FacilityType.get_by_key_name(self.facility.type,
    self.version)
self.attributes = dict((a.key().name(), a) for a in model.Attribute.all().
    ancestor(self.version))
self.readonly_attribute_names = ['healthc_id']
