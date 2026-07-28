def get_replicated_engine(name, order_by=settings.DEFAULT_ORDER_BY,...
return """
        ReplicatedReplacingMergeTree('/clickhouse/tables/{shard}/%(name)s', '{replica}', %(version_column)s)
        PARTITION BY %(partition_by)s
        ORDER BY %(order_by)s
        SAMPLE BY %(sample_expr)s;""" % {
    'name': name, 'order_by': order_by, 'partition_by': partition_by,
    'version_column': version_column, 'sample_expr': sample_expr}
