def raw_query(body, sql, client, timer, stats=None):...
"""docstring"""
project_ids = to_list(body['project'])
project_id = project_ids[0] if project_ids else 0
stats = stats or {}
grl, gcl, prl, pcl, use_cache = state.get_configs([(
    'global_per_second_limit', 1000), ('global_concurrent_limit', 1000), (
    'project_per_second_limit', 1000), ('project_concurrent_limit', 1000),
    ('use_cache', 0)])
prl, pcl = state.get_configs([('project_per_second_limit_{}'.format(
    project_id), prl), ('project_concurrent_limit_{}'.format(project_id), pcl)]
    )
all_confs = six.iteritems(state.get_all_configs())
query_settings = {k.split('/', 1)[1]: v for k, v in all_confs if k.
    startswith('query_settings/')}
timer.mark('get_configs')
query_id = md5(force_bytes(sql)).hexdigest()
timer.mark('dedupe_wait')
result = state.get_result(query_id) if use_cache else None
timer.mark('cache_get')
stats.update({'is_duplicate': is_dupe, 'query_id': query_id, 'use_cache':
    bool(use_cache), 'cache_hit': bool(result)}),
if result:
status = 200
metrics.gauge('query.global_concurrent', g_concurr)
stats.update(query_settings)
stats.update({'global_rate': g_rate, 'global_concurrent': g_concurr})
state.record_query({'request': body, 'sql': sql, 'timing': timer, 'stats':
    stats, 'status': status})
stats.update({'project_rate': p_rate, 'project_concurrent': p_concurr})
if settings.RECORD_QUERIES:
timer.mark('rate_limit')
timer.send_metrics_to(metrics)
result['timing'] = timer
if g_allowed and p_allowed:
if settings.STATS_IN_RESPONSE or body.get('debug', False):
if 'max_threads' in query_settings and p_concurr > 1:
status = 429
result['stats'] = stats
return result, status
maxt = query_settings['max_threads']
data, meta = client.execute(sql, with_column_types=True, settings=
    query_settings, query_id=query_id)
error = six.text_type(ex)
result = {'error': {'type': 'ratelimit', 'message': 'rate limit exceeded'}}
result['sql'] = sql
query_settings['max_threads'] = max(1, maxt - p_concurr + 1)
data, meta = scrub_ch_data(data, meta)
status = 500
status = 200
logger.error("""Error running query: %s
%s""", sql, error)
if body.get('totals', False):
if isinstance(ex, ClickHouseError):
assert len(data) > 0
result = {'data': data, 'meta': meta}
result = {'error': {'type': 'clickhouse', 'code': ex.code, 'message': error}}
result = {'error': {'type': 'unknown', 'message': error}}
data, totals = data[:-1], data[-1]
logger.debug(sql)
result = {'data': data, 'meta': meta, 'totals': totals}
timer.mark('execute')
stats.update({'result_rows': len(data), 'result_cols': len(meta)})
if use_cache:
state.set_result(query_id, result)
timer.mark('cache_set')
