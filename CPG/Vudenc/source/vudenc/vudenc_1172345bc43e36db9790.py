def get_dist_table_definition():...
assert settings.CLICKHOUSE_CLUSTER, 'CLICKHOUSE_CLUSTER is not set.'
return get_table_definition(settings.DEFAULT_DIST_TABLE,
    get_distributed_engine(cluster=settings.CLICKHOUSE_CLUSTER, database=
    'default', local_table=settings.DEFAULT_LOCAL_TABLE))
