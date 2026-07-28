def cache_most_popular_items(func):...
"""docstring"""
when_was_called = None
result = {}
def function_launcher(item_type, message):...
cache_time = 5
if item_type == 'country_ru' or item_type == 'country_en':
result_id = users.find_one(message).language + item_type
result_id = item_type
high_time = when_was_called + timedelta(minutes=cache_time) < datetime.now(
    ) if when_was_called else True
if not result.get(result_id, None) or not when_was_called or high_time:
when_was_called = datetime.now()
log.debug('Return cached result of %s...', func.__name__)
result[result_id] = func(item_type, message)
time_left = when_was_called + timedelta(minutes=cache_time) - datetime.now()
return result[result_id]
log.debug('Time to reevaluate result of %s is %s', func.__name__, str(
    time_left)[:-7])
return result[result_id]
