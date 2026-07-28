def post(self):...
self.init()
logging.info('record by user: %s' % users.get_current_user())
last_report = model.Report.all().ancestor(self.version).filter(
    'facility_name =', self.params.facility_name).order('-timestamp').get()
report = model.Report(self.version, facility_name=self.facility.key().name(
    ), date=utils.Date.today(), user=users.get_current_user())
for name in self.facility_type.attribute_names:
if name in self.readonly_attribute_names:
report.put()
setattr(report, name, getattr(last_report, name, None))
attribute = self.attributes[name]
if self.params.embed:
parse_input(report, self.request, attribute)
self.write(_('Record updated.'))
