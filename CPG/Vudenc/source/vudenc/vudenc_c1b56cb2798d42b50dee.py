def get_nodes(self):...
if self.get_option('no-hypervisors'):
return []
res = self.exec_master_cmd(self.dbcmd, need_root=True)
if res['status'] == 0:
nodes = res['stdout'].splitlines()[2:-1]
return [n.split('(')[0].strip() for n in nodes]
