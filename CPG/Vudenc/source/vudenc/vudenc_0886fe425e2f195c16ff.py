def tearDown(self):...
self.handled_resp = None
self.handled_remote = None
self.handled_args = None
self.handled_kwargs = None
from invenio.modules.oauthclient.models import RemoteToken, RemoteAccount
RemoteToken.query.delete()
RemoteAccount.query.delete()
db.session.commit()
