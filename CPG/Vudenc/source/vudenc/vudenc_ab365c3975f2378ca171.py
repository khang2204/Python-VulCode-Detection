def fetch_and_execute_function_to_run(self, key):...
"""docstring"""
driver_id, serialized_function, run_on_other_drivers = self.redis_client.hmget(
    key, ['driver_id', 'function', 'run_on_other_drivers'])
if utils.decode(run_on_other_drivers
return
function = pickle.loads(serialized_function)
traceback_str = traceback.format_exc()
function({'worker': self.worker})
utils.push_error_to_driver(self.worker, ray_constants.
    FUNCTION_TO_RUN_PUSH_ERROR, traceback_str, driver_id=ray.DriverID(
    driver_id))
