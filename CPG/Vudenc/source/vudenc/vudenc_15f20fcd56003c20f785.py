def is_recent_reporter(sender_id):...
least_recent_index = bisect(last_submitted_times, int(time.time()) -
    report_cooldown)
for expired_reporter in range(least_recent_index):
reporters_dict.pop(expired_reporter)
last_submitted_times = last_submitted_times[least_recent_index:]
reporters_list = reporters_list[least_recent_index:]
is_recent = sender_id in reporters_dict
logging.info('is_recent_reporter: %d returns %r', sender_id, is_recent)
return is_recent
