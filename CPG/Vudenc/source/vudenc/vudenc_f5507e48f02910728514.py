def get_distributed_engine(cluster, database, local_table, sharding_key=...
return 'Distributed(%(cluster)s, %(database)s, %(local_table)s, %(sharding_key)s);' % {
    'cluster': cluster, 'database': database, 'local_table': local_table,
    'sharding_key': sharding_key}
