def retrieveNextInsertId(self, klass):...
seqname = '%s_%s_seq' % (klass.name(), klass.sqlSerialColumnName())
conn, curs = self.executeSQL("select nextval('%s')" % seqname)
value = curs.fetchone()[0]
assert value, "Didn't get next id value from sequence"
return value
