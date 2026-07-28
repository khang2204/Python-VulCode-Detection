def main():...
module = AnsibleModule(argument_spec=dict(login_user=dict(default=
    'postgres'), login_password=dict(default='', no_log=True), login_host=
    dict(default=''), login_unix_socket=dict(default=''), port=dict(default
    ='5432'), option=dict(required=True, aliases=['name', 'setting', 'guc',
    'parameter']), value=dict(default=''), state=dict(default='present',
    choices=['absent', 'present'])), supports_check_mode=True)
if not postgresqldb_found:
module.fail_json(msg='the python psycopg2 module is required')
option = module.params['option']
value = module.params['value']
port = module.params['port']
state = module.params['state']
changed = False
params_map = {'login_host': 'host', 'login_user': 'user', 'login_password':
    'password', 'port': 'port'}
kw = dict((params_map[k], v) for k, v in iteritems(module.params) if k in
    params_map and v != '')
if 'host' not in kw or kw['host'] == '' or kw['host'] == 'localhost':
is_localhost = True
is_localhost = False
if is_localhost and module.params['login_unix_socket'] != '':
kw['host'] = module.params['login_unix_socket']
db_connection = psycopg2.connect(database='postgres', **kw)
e = get_exception()
if option_ispreset(cursor, option):
e = get_exception()
module.exit_json(changed=changed, option=option)
if psycopg2.__version__ >= '2.4.2':
module.fail_json(msg='unable to connect to database: %s' % e)
module.warn(
    'Option %s is preset, so it can only be set at initdb or before building from source code. For details, see postgresql.org/docs/current/static/runtime-config-preset.html'
     % option)
if option_exists(cursor, option):
module.fail_json(msg=str(e))
db_connection.autocommit = True
db_connection.set_isolation_level(psycopg2.extensions.
    ISOLATION_LEVEL_AUTOCOMMIT)
if module.check_mode:
module.warn('Option %s does not exist' % option)
e = get_exception()
cursor = db_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
if state == 'absent':
if state == 'absent':
module.fail_json(msg='Database query failed: %s' % e)
changed = not option_isdefault(cursor, option)
if state == 'present':
if state == 'present':
changed = option_reset(cursor, option)
e = get_exception()
module.exit_json(changed=changed, option=option)
changed = not option_matches(cursor, option, value)
changed = option_set(cursor, option, value)
e = get_exception()
module.fail_json(msg=str(e))
module.fail_json(msg=str(e))
