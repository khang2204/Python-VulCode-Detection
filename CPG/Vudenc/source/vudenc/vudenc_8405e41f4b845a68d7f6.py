def log_unexpected_subset_keys(expected_keys, minimum_keys, actual_keys,...
"""docstring"""
message = has_unexpected_subset_keys(expected_keys, minimum_keys,
    actual_keys, name)
if message:
ereporter2.log_request(request, source=source, message=message)
return message
