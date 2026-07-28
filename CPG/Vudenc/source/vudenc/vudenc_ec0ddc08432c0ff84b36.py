@auth.autologin...
"""docstring"""
end = int(float(self.request.get('end', 0)) or time.time())
start = int(float(self.request.get('start', 0)) or ui.
    _get_default_start_time() or 0)
modules = self.request.get('modules')
if modules:
modules = modules.split(',')
tainted = bool(int(self.request.get('tainted', '1')))
module_versions = utils.get_module_version_list(modules, tainted)
errors, ignored, _end_time = logscraper.scrape_logs_for_errors(start, end,
    module_versions)
params = {'errors': errors, 'errors_count': sum(len(e.events) for e in
    errors), 'errors_version_count': len(set(itertools.chain.from_iterable(
    e.versions for e in errors))), 'ignored': ignored, 'ignored_count': sum
    (len(i.events) for i in ignored), 'ignored_version_count': len(set(
    itertools.chain.from_iterable(i.versions for i in ignored))),
    'xsrf_token': self.generate_xsrf_token()}
params.update(ui._get_template_env(start, end, module_versions))
self.response.write(template.render('ereporter2/requests.html', params))
