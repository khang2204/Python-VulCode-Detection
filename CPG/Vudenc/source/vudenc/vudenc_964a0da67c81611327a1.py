@defer.inlineCallbacks...
if os.path.isdir(tempdir):
shutil.rmtree(tempdir)
passphrase = u'verysecretpassphrase'
secret_path = os.path.join(tempdir, 'secret.gpg')
local_db_path = os.path.join(tempdir, 'soledad.u1db')
server_url = 'http://provider'
cert_file = ''
get_doc = Mock(return_value=None)
put_doc = Mock()
lock = Mock(return_value=('atoken', 300))
unlock = Mock(return_value=True)
close = Mock()
def __call__(self):...
return self
