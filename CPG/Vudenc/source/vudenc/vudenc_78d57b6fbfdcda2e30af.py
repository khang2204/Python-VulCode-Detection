def check_cve(self, request, obj):...
errors = list()
test = True
for probe in obj:
if test:
probe.check_cve()
test = False
messages.add_message(request, messages.SUCCESS, 'Check CVE OK')
messages.add_message(request, messages.ERROR, 'Check CVE failed ! ' + str(
    errors))
logger.exception('Error in check_cve ' + str(self.actions))
errors.append(str(e))
