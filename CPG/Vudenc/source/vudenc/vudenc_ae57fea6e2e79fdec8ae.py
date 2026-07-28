def get_test_engine(order_by=settings.DEFAULT_ORDER_BY, partition_by=...
return """
        ReplacingMergeTree(%(version_column)s)
        PARTITION BY %(partition_by)s
        ORDER BY %(order_by)s
        SAMPLE BY %(sample_expr)s ;""" % {
    'order_by': settings.DEFAULT_ORDER_BY, 'partition_by': settings.
    DEFAULT_PARTITION_BY, 'version_column': settings.DEFAULT_VERSION_COLUMN,
    'sample_expr': settings.DEFAULT_SAMPLE_EXPR}
