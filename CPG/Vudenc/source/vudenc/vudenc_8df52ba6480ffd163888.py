def _process(self):...
"""docstring"""
request = self.parse_body()
version = request.get('version', None)
dimensions = request.get('dimensions', {})
state = request.get('state', {})
bot_id = None
if dimensions.get('id'):
dimension_id = dimensions['id']
if bool(dimensions.get('quarantined')) or bool(state.get('quarantined')):
if isinstance(dimension_id, list) and len(dimension_id) == 1 and isinstance(
return request, bot_id, version, state, dimensions, 'Bot self-quarantined'
quarantined_msg = None
bot_id = dimensions['id'][0]
for _ in [0]:
quarantined_msg = has_unexpected_keys(self.EXPECTED_KEYS, request, 'keys')
if quarantined_msg:
if quarantined_msg:
line = """Quarantined Bot
https://%s/restricted/bot/%s
%s""" % (app_identity
    .get_default_version_hostname(), bot_id, quarantined_msg)
bot_settings = bot_management.get_settings_key(bot_id).get()
quarantined_msg = has_missing_keys(self.REQUIRED_STATE_KEYS, state, 'state')
ereporter2.log_request(self.request, source='bot', message=line)
if bool(bot_settings and bot_settings.quarantined):
if quarantined_msg:
return request, bot_id, version, state, dimensions, quarantined_msg
return request, bot_id, version, state, dimensions, 'Quarantined by admin'
return request, bot_id, version, state, dimensions, None
if not bot_id:
quarantined_msg = 'Missing bot id'
if not all(isinstance(key, unicode) and isinstance(values, list) and all(
quarantined_msg = """Invalid dimensions type:
%s""" % json.dumps(dimensions,
    sort_keys=True, indent=2, separators=(',', ': '))
dimensions_count = task_to_run.dimensions_powerset_count(dimensions)
if dimensions_count > task_to_run.MAX_DIMENSIONS:
quarantined_msg = 'Dimensions product %d is too high' % dimensions_count
if not isinstance(state.get('lease_expiration_ts'), (None.__class__, int)):
quarantined_msg = 'lease_expiration_ts (%r) must be int or None' % state[
    'lease_expiration_ts']
