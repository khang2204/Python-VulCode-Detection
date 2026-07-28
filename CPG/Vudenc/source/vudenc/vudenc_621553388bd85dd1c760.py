"""HTTP Handlers."""
import datetime
import itertools
import json
import time
import webapp2
from google.appengine.api import app_identity
from google.appengine.datastore import datastore_query
from google.appengine.ext import ndb
from components import auth
from components import decorators
from components import template
from components import utils
from . import acl
from . import logscraper
from . import models
from . import on_error
from . import ui
"""Returns all the recent errors as a web page."""
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
"""Dumps information about single logged request."""
@auth.autologin...
data = logscraper._log_request_id(request_id)
if not data:
self.abort(404, detail='Request id was not found.')
self.response.write(template.render('ereporter2/request.html', {'request':
    data}))
"""Dumps information about reported client side errors."""
@auth.autologin...
limit = int(self.request.get('limit', 100))
cursor = datastore_query.Cursor(urlsafe=self.request.get('cursor'))
errors_found, cursor, more = models.Error.query().order(-models.Error.
    created_ts).fetch_page(limit, start_cursor=cursor)
params = {'cursor': cursor.urlsafe() if cursor and more else None, 'errors':
    errors_found, 'limit': limit, 'now': utils.utcnow()}
self.response.out.write(template.render('ereporter2/errors.html', params))
"""Dumps information about reported client side errors."""
@auth.autologin...
error = models.Error.get_by_id(int(error_id))
if not error:
self.abort(404, 'Error not found')
params = {'error': error, 'now': utils.utcnow()}
self.response.out.write(template.render('ereporter2/error.html', params))
@auth.autologin...
items = models.ErrorReportingMonitoring.query().fetch()
items.sort(key=lambda x: x.created_ts)
params = {'silenced': items, 'xsrf_token': self.generate_xsrf_token()}
self.response.out.write(template.render('ereporter2/silence.html', params))
@auth.require(acl.is_ereporter2_editor)...
to_delete = self.request.get('to_delete')
if to_delete:
ndb.Key(models.ErrorReportingMonitoring, to_delete).delete()
mute_type = self.request.get('mute_type')
self.get()
error = None
"""Generate and emails an exception report."""
if mute_type in ('exception_type', 'signature'):
@decorators.require_cronjob...
error = self.request.get(mute_type)
if not error:
"""docstring"""
self.abort(400)
silenced = self.request.get('silenced')
host_url = 'https://%s.appspot.com' % app_identity.get_application_id()
silenced_until = self.request.get('silenced_until')
request_id_url = host_url + '/restricted/ereporter2/request/'
if silenced_until == 'T':
report_url = host_url + '/restricted/ereporter2/report'
silenced_until = ''
threshold = self.request.get('threshold')
recipients = self.request.get('recipients', acl.get_ereporter2_recipients())
key = models.ErrorReportingMonitoring.error_to_key(error)
result = ui._generate_and_email_report(utils.get_module_version_list(None, 
    False), recipients, request_id_url, report_url, {})
if not silenced and not silenced_until and not threshold:
self.response.headers['Content-Type'] = 'text/plain; charset=utf-8'
key.delete()
item = models.ErrorReportingMonitoring(key=key, error=error)
if result:
if silenced:
self.response.write('Success.')
self.response.write('Failed.')
item.silenced = True
if silenced_until:
"""Deletes old error reports."""
item.silenced_until = datetime.datetime.strptime(silenced_until,
    '%Y-%m-%dT%H:%M')
if threshold:
@decorators.require_cronjob...
item.threshold = int(threshold)
item.put()
old_cutoff = utils.utcnow() - on_error.ERROR_TIME_TO_LIVE
items = models.Error.query(models.Error.created_ts < old_cutoff,
    default_options=ndb.QueryOptions(keys_only=True))
out = len(ndb.delete_multi(items))
self.response.headers['Content-Type'] = 'text/plain; charset=utf-8'
self.response.write(str(out))
"""Adds an error report.

  This one is open so errors like authentication reports are logged in too.
  This means we could get spammed a lot about it. Implement DDoS protection by
  rate limiting once a kid figures out.
  """
xsrf_token_enforce_on = ()
def parse_body(self):...
"""docstring"""
expected = 'application/json', 'application/json; charset=utf-8'
if self.request.headers.get('Content-Type').lower() not in expected:
msg = "Expecting JSON body with content type 'application/json'"
body = json.loads(self.request.body)
self.abort(400, 'Not a valid json dict body')
return body
self.abort(400, msg)
if not isinstance(body, dict):
