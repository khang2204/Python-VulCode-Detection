def push_error_to_driver(worker, error_type, message, driver_id=None):...
"""docstring"""
if driver_id is None:
driver_id = ray.DriverID.nil()
worker.raylet_client.push_error(driver_id, error_type, message, time.time())
