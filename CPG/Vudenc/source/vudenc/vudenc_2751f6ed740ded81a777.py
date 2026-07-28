def collect(self):...
"""docstring"""
if self.master.connected:
self.client_list.append(self.master)
self.console.info("""
Connecting to nodes...""")
filters = [self.master.address, self.master.hostname]
nodes = [n for n in self.node_list if n not in filters]
pool = ThreadPoolExecutor(self.config['threads'])
self.log_error('Exiting on user cancel\n')
if hasattr(self.config['cluster'], 'run_extra_cmd'):
pool.map(self._connect_to_node, nodes, chunksize=1)
os._exit(130)
self.console.info('Collecting additional data from master node...')
msg = """
Successfully captured %s of %s sosreports"""
pool.shutdown(wait=True)
files = self.config['cluster']._run_extra_cmd()
self.log_info(msg % (self.retrieved, self.report_num))
self.report_num = len(self.client_list)
if files:
if self.retrieved > 0:
if self.config['no_local'] and self.master.address == 'localhost':
self.master.collect_extra_cmd(files)
self.create_cluster_archive()
msg = 'No sosreports were collected, nothing to archive...'
self.report_num -= 1
self.console.info(
    """
Beginning collection of sosreports from %s nodes, collecting a maximum of %s concurrently
"""
     % (self.report_num, self.config['threads']))
self.close_all_connections()
self._exit(msg, 1)
pool = ThreadPoolExecutor(self.config['threads'])
pool.map(self._collect, self.client_list, chunksize=1)
pool.shutdown(wait=True)
