def __init__(self):...
self.connect_params = dict(database=const.get_const('db-name'), user=const.
    get_const('db-user'), password=const.get_const('db-password'), host=
    const.get_const('db-host-addr'), port=const.get_const('db-host-port'))
self._db = psycopg2.connect(**self.connect_params)
self._cur = None
return
