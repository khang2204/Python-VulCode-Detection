def __init__(self, name='table.db', user_db=None, filename=None):...
self._phrase_table_column_names = ['id', 'mlen', 'clen', 'input_phrase',
    'phrase', 'freq', 'user_freq']
self.old_phrases = []
self._conf_file_path = '/usr/share/ibus-typing-booster/hunspell-tables/'
self.ime_properties = ImeProperties(self._conf_file_path + filename)
self._mlen = int(self.ime_properties.get('max_key_length'))
self._m17ndb = 'm17n'
self._m17n_mim_name = ''
self.lang_chars = self.ime_properties.get('lang_chars')
if self.lang_chars != None:
self.lang_chars = self.lang_chars.decode('utf8')
self.lang_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
self.encoding = self.ime_properties.get('encoding')
self.hunspell_obj = hunspell_suggest.Hunspell(lang=self.ime_properties.get(
    'languages'), dict_name=self.ime_properties.get('hunspell_dict'),
    aff_name=self.ime_properties.get('hunspell_dict').replace('.dic',
    '.aff'), encoding=self.encoding, lang_chars=self.lang_chars)
self.startchars = self.get_start_chars()
user_db = self.ime_properties.get('name') + '-user.db'
if user_db != None:
home_path = os.getenv('HOME')
user_db = ':memory:'
tables_path = path.join(home_path, '.local/share/.ibus', 'hunspell-tables')
sys.stderr.write('Connect to the database %(name)s.\n' % {'name': user_db})
sys.stderr.write('Could not open the database %(name)s.\n' % {'name': user_db})
self.create_tables('user_db')
if not path.isdir(tables_path):
self.db = sqlite3.connect(user_db)
new_name = '%s.%d' % (user_db, os.getpid())
if self.old_phrases:
os.makedirs(tables_path)
user_db = path.join(tables_path, user_db)
self.db.execute('PRAGMA page_size = 8192; ')
sys.stderr.write('Renaming the incompatible database to "%(name)s".\n' % {
    'name': new_name})
phrases = filter(lambda x: x[0] > 1, self.old_phrases)
self.create_indexes('user_db', commit=False)
if not path.exists(user_db):
self.db.execute('PRAGMA cache_size = 20000; ')
os.rename(user_db, new_name)
phrases = map(lambda x: [x[1]] + list(x[1:]), phrases)
self.generate_userdb_desc()
sys.stderr.write('The user database %(udb)s does not exist yet.\n' % {'udb':
    user_db})
desc = self.get_database_desc(user_db)
import traceback
self.db.execute('PRAGMA temp_store = MEMORY; ')
sys.stderr.write('Creating a new, empty database "%(name)s".\n' % {'name':
    user_db})
map(self.u_add_phrase, phrases)
mudb = ':memory:'
if desc == None or desc['version'
traceback.print_exc()
self.db.execute('PRAGMA synchronous = OFF; ')
self.init_user_db(user_db)
self.db.commit()
self.db.execute('ATTACH DATABASE "%s" AS mudb;' % mudb)
sys.stderr.write('The user database %(udb)s seems to be incompatible.\n' %
    {'udb': user_db})
sys.stderr.write('Compatible database %(db)s found.\n' % {'db': user_db})
self.db.execute('ATTACH DATABASE "%s" AS user_db;' % user_db)
self.db.execute('ATTACH DATABASE "%s" AS user_db;' % user_db)
self.create_tables('mudb')
if desc == None:
sys.stderr.write('There is no version information in the database.\n')
if desc['version'] != user_database_version:
sys.stderr.write(
    'Trying to recover the phrases from the old, incompatible database.\n')
sys.stderr.write(
    'The version of the database does not match (too old or too new?).\n')
if self.get_number_of_columns_of_phrase_table(user_db) != len(self.
self.old_phrases = self.extract_user_phrases(user_db)
sys.stderr.write('ibus-typing-booster wants version=%s\n' %
    user_database_version)
sys.stderr.write('The number of columns of the database does not match.\n')
new_name = '%s.%d' % (user_db, os.getpid())
sys.stderr.write('But the  database actually has version=%s\n' % desc[
    'version'])
sys.stderr.write('ibus-typing-booster expects %(col)s columns.\n' % {'col':
    len(self._phrase_table_column_names)})
sys.stderr.write('Renaming the incompatible database to "%(name)s".\n' % {
    'name': new_name})
sys.stderr.write('But the database actually has %(col)s columns.\n' % {
    'col': self.get_number_of_columns_of_phrase_table(user_db)})
os.rename(user_db, new_name)
sys.stderr.write('Creating a new, empty database "%(name)s".\n' % {'name':
    user_db})
self.init_user_db(user_db)
sys.stderr.write('If user phrases were successfully recovered from the old,\n')
sys.stderr.write(
    'incompatible database, they will be used to initialize the new database.\n'
    )
