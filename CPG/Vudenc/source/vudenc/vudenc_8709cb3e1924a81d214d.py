def parse_db_conf(self):...
conf = {}
engconf = '/etc/ovirt-engine/engine.conf.d/10-setup-database.conf'
res = self.exec_master_cmd('cat %s' % engconf, need_root=True)
if res['status'] == 0:
config = res['stdout'].splitlines()
return False
for line in config:
return conf
k = str(line.split('=')[0])
v = str(line.split('=')[1].replace('"', ''))
conf[k] = v
