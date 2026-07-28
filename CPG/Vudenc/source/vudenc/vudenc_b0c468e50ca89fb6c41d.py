def get(self):...
self.init()
fields = []
readonly_fields = [{'name': 'ID', 'value': self.params.facility_name}]
report = model.Report.all().ancestor(self.version).filter('facility_name =',
    self.params.facility_name).order('-timestamp').get()
for name in self.facility_type.attribute_names:
attribute = self.attributes[name]
self.render('templates/edit.html', facility=self.facility, fields=fields,
    readonly_fields=readonly_fields, params=self.params, authorization=self
    .auth and self.auth.description or 'anonymous', logout_url=users.
    create_logout_url('/'))
if name in self.readonly_attribute_names:
readonly_fields.append({'name': get_message(self.version, 'attribute_name',
    name), 'value': getattr(report, name, None)})
fields.append({'name': get_message(self.version, 'attribute_name', name),
    'type': attribute.type, 'input': make_input(self.version, report,
    attribute)})
