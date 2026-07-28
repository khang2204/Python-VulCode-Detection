def check_phrase(self, phrase, input_phrase=None, database='main'):...
"""docstring"""
if type(phrase) != type(u''):
phrase = phrase.decode('utf8')
if type(input_phrase) != type(u''):
input_phrase = input_phrase.decode('utf8')
if len(phrase) < 4:
return
sqlstr = (
    """
                SELECT * FROM user_db.phrases WHERE phrase = "%(phrase)s" and input_phrase = "%(input_phrase)s"
                UNION ALL
                SELECT * FROM mudb.phrases WHERE phrase = "%(phrase)s" and input_phrase = "%(input_phrase)s"
                ORDER BY user_freq DESC, freq DESC, id ASC;"""
     % {'phrase': phrase, 'input_phrase': input_phrase})
result = self.db.execute(sqlstr).fetchall()
filter(lambda x: x[-3] == phrase and result.append(tuple(x)), self.
    hunspell_obj.suggest(input_phrase))
if len(result) == 0:
self.add_phrase((input_phrase, phrase, -2, 1), database='mudb')
sysdb = {}
usrdb = {}
mudb = {}
map(lambda x: sysdb.update([(x[3:-2], x[:])]), filter(lambda x: not x[-1],
    result))
map(lambda x: usrdb.update([(x[3:-2], x[:])]), filter(lambda x: x[-2] in [0,
    -1] and x[-1], result))
map(lambda x: mudb.update([(x[3:-2], x[:])]), filter(lambda x: x[-2] not in
    [0, -1] and x[-1], result))
map(usrdb.pop, filter(lambda key: key in mudb, usrdb.keys()))
map(sysdb.pop, filter(lambda key: key in mudb or key in usrdb, sysdb.keys()))
map(lambda res: self.add_phrase((res[0], phrase, -3 if usrdb[res][-2] == -1
     else 1, usrdb[res][-1] + 1), database='mudb'), usrdb.keys())
map(lambda res: self.add_phrase((res[0], phrase, 2, 1), database='mudb'),
    sysdb.keys())
map(lambda key: self.update_phrase((mudb[key][3], mudb[key][4], mudb[key][5
    ], mudb[key][6] + 1), database='mudb'), mudb.keys())
