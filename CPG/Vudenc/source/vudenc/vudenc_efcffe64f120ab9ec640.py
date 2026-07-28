def collect_database(self):...
sos_opt = (
    '-k {plugin}.dbname={db} -k {plugin}.dbhost={dbhost} -k {plugin}.dbport={dbport} -k {plugin}.username={dbuser} '
    .format(plugin='postgresql', db=self.conf['ENGINE_DB_DATABASE'], dbhost
    =self.conf['ENGINE_DB_HOST'], dbport=self.conf['ENGINE_DB_PORT'],
    dbuser=self.conf['ENGINE_DB_USER']))
cmd = (
    'PGPASSWORD={} /usr/sbin/sosreport --name=postgresql --batch -o postgresql {}'
    .format(self.conf['ENGINE_DB_PASSWORD'], sos_opt))
db_sos = self.exec_master_cmd(cmd, need_root=True)
for line in db_sos['stdout'].splitlines():
if fnmatch.fnmatch(line, '*sosreport-*tar*'):
self.log_error('Failed to gather database dump')
return line.strip()
return False
