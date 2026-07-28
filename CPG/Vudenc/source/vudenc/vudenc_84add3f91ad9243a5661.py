def _process_key(self, key):...
"""docstring"""
if self.mode != ray.WORKER_MODE:
if key.startswith(b'FunctionsToRun'):
if key.startswith(b'RemoteFunction'):
self.fetch_and_execute_function_to_run(key)
return
self.worker.function_actor_manager.fetch_and_register_remote_function(key)
if key.startswith(b'FunctionsToRun'):
self.fetch_and_execute_function_to_run(key)
if key.startswith(b'ActorClass'):
self.worker.function_actor_manager.imported_actor_classes.add(key)
