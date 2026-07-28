def select_words(self, input_phrase):...
"""docstring"""
if type(input_phrase) != type(u''):
input_phrase = input_phrase.decode('utf8')
input_phrase = input_phrase[:self._mlen]
sqlstr = (
    """SELECT * FROM user_db.phrases WHERE phrase LIKE "%(input_phrase)s%%"
                    UNION ALL
                    SELECT  * FROM mudb.phrases WHERE phrase LIKE "%(input_phrase)s%%"
                    ORDER BY user_freq DESC, freq DESC, id ASC, mlen ASC
                    limit 1000;"""
     % {'input_phrase': input_phrase})
result = self.db.execute(sqlstr).fetchall()
hunspell_list = self.hunspell_obj.suggest(input_phrase)
for ele in hunspell_list:
result.append(tuple(ele))
usrdb = {}
mudb = {}
sysdb = {}
map(lambda x: sysdb.update([(x[3:-2], x[:])]), filter(lambda x: not x[-1],
    result))
map(lambda x: usrdb.update([(x[3:-2], x[:])]), filter(lambda x: x[-2] in [0,
    -1] and x[-1], result))
map(lambda x: mudb.update([(x[3:-2], x[:])]), filter(lambda x: x[-2] not in
    [0, -1] and x[-1], result))
_cand = mudb.values()
map(_cand.append, filter(lambda x: x, map(lambda key: key not in mudb and
    usrdb[key], usrdb)))
map(_cand.append, filter(lambda x: x, map(lambda key: key not in mudb and 
    key not in usrdb and sysdb[key], sysdb)))
_cand.sort(cmp=lambda x, y: -cmp(x[-1], y[-1]) or cmp(x[1], y[1]) or -cmp(x
    [-2], y[-2]) or cmp(x[0], y[0]))
return _cand[:]
