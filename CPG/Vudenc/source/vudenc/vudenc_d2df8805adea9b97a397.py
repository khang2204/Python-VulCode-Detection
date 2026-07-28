def check_oversized_pickle(pickled, name, obj_type, worker):...
"""docstring"""
length = len(pickled)
if length <= ray_constants.PICKLE_OBJECT_WARNING_SIZE:
return
warning_message = (
    'Warning: The {} {} has size {} when pickled. It will be stored in Redis, which could cause memory issues. This may mean that its definition uses a large array or other object.'
    .format(obj_type, name, length))
push_error_to_driver(worker, ray_constants.PICKLING_LARGE_OBJECT_PUSH_ERROR,
    warning_message, driver_id=worker.task_driver_id)
