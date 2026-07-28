@staticmethod...
if obj.last_run_at:
return obj.schedule.remaining_estimate(last_run_at=obj.last_run_at)
z, y = obj.schedule.is_due(last_run_at=datetime.now(pytz.utc))
date = datetime.now(pytz.utc) + timedelta(seconds=y)
return date
