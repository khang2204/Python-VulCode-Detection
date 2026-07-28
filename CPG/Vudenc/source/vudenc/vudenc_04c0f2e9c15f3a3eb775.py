def push_error_to_driver_through_redis(redis_client, error_type, message,...
"""docstring"""
if driver_id is None:
driver_id = ray.DriverID.nil()
error_data = ray.gcs_utils.construct_error_message(driver_id, error_type,
    message, time.time())
redis_client.execute_command('RAY.TABLE_APPEND', ray.gcs_utils.TablePrefix.
    ERROR_INFO, ray.gcs_utils.TablePubsub.ERROR_INFO, driver_id.binary(),
    error_data)
