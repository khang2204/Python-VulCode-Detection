def _cmd_run(self, request, run_result_key, bot_id):...
cmd = None
if request.properties.commands:
cmd = request.properties.commands[0]
if request.properties.command:
out = {'cmd': 'run', 'manifest': {'bot_id': bot_id, 'command': cmd,
    'dimensions': request.properties.dimensions, 'env': request.properties.
    env, 'extra_args': request.properties.extra_args, 'grace_period':
    request.properties.grace_period_secs, 'hard_timeout': request.
    properties.execution_timeout_secs, 'host': utils.get_versioned_hosturl(
    ), 'io_timeout': request.properties.io_timeout_secs, 'inputs_ref':
    request.properties.inputs_ref, 'task_id': task_pack.pack_run_result_key
    (run_result_key)}}
cmd = request.properties.command
self.send_response(utils.to_json_encodable(out))
