def format_db_cmd(self):...
cluster = self.get_option('cluster') or '%'
datacenter = self.get_option('datacenter') or '%'
self.dbcmd = '/usr/share/ovirt-engine/dbscripts/engine-psql.sh -c "'
self.dbcmd += (
    'select host_name from vds_static where cluster_id in (select cluster_id from cluster where name like \'%s\' and storage_pool_id in (select id from storage_pool where name like \'%s\'))"'
     % (cluster, datacenter))
self.log_debug('Query command for ovirt DB set to: %s' % self.dbcmd)
