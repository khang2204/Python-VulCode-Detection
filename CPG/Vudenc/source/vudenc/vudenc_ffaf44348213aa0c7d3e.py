def cache_number_users_with_same_feature(func):...
when_was_called = None
result = {}
def func_launcher(feature, feature_type):...
cache_time = 5
high_time = when_was_called + timedelta(minutes=cache_time) < datetime.now(
    ) if when_was_called else True
if not when_was_called or high_time or feature not in result:
when_was_called = datetime.now()
log.info('Returning cached result of %s', func.__name__)
num_of_users = func(feature, feature_type)
time_left = when_was_called + timedelta(minutes=cache_time) - datetime.now()
result[feature] = num_of_users
log.debug('Time to to reevaluate result of %s is %s', func.__name__, str(
    time_left)[:-7])
return num_of_users
return result[feature]
