@staticmethod...
if obj.last_run_at:
return obj.schedule.remaining_estimate(last_run_at=obj.last_run_at)
return obj.schedule.remaining_estimate(last_run_at=datetime.now(pytz.utc))
