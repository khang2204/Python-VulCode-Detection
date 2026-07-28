def post_update(swarming_server, params, exit_code, stdout, output_chunk_start...
"""docstring"""
params = params.copy()
if exit_code is not None:
params['exit_code'] = exit_code
if stdout:
params['output'] = base64.b64encode(stdout)
resp = swarming_server.url_read_json('/swarming/api/v1/bot/task_update/%s' %
    params['task_id'], data=params)
params['output_chunk_start'] = output_chunk_start
logging.debug('post_update() = %s', resp)
if resp.get('error'):
