import os
import fnmatch
from soscollector.clusters import Cluster
from getpass import getpass
packages = 'ovirt-engine',
option_list = [('no-database', False, 'Do not collect a database dump'), (
    'cluster', '', 'Only collect from hosts in this cluster'), (
    'datacenter', '', 'Only collect from hosts in this datacenter'), (
    'no-hypervisors', False, 'Do not collect from hypervisors')]
def setup(self):...
self.pg_pass = False
if not self.get_option('no-database'):
self.conf = self.parse_db_conf()
self.format_db_cmd()
def format_db_cmd(self):...
cluster = self.get_option('cluster') or '%'
datacenter = self.get_option('datacenter') or '%'
self.dbcmd = '/usr/share/ovirt-engine/dbscripts/engine-psql.sh -c "'
self.dbcmd += (
    'select host_name from vds_static where cluster_id in (select cluster_id from cluster where name like \'%s\' and storage_pool_id in (select id from storage_pool where name like \'%s\'))"'
     % (cluster, datacenter))
self.log_debug('Query command for ovirt DB set to: %s' % self.dbcmd)
def get_nodes(self):...
if self.get_option('no-hypervisors'):
return []
res = self.exec_master_cmd(self.dbcmd, need_root=True)
if res['status'] == 0:
nodes = res['stdout'].splitlines()[2:-1]
def run_extra_cmd(self):...
return [n.split('(')[0].strip() for n in nodes]
if not self.get_option('no-database') and self.conf:
return self.collect_database()
return False
