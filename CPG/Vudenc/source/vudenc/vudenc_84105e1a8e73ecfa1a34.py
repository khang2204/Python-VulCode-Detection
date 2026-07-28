def call_handler(cls, *args, **kw):...
if not GLSetting.memory_copy.anomaly_checks:
return method_handler(cls, *args, **kw)
if GLSetting.anomalies_counter[element] > alarm_level[element]:
if element == 'new_submission':
return method_handler(cls, *args, **kw)
log.debug('Blocked a New Submission (%d > %d)' % (GLSetting.
    anomalies_counter[element], alarm_level[element]))
if element == 'finalized_submission':
log.debug('Blocked a Finalized Submission (%d > %d)' % (GLSetting.
    anomalies_counter[element], alarm_level[element]))
if element == 'anon_requests':
log.debug('Blocked an Anon Request (%d > %d)' % (GLSetting.
    anomalies_counter[element], alarm_level[element]))
if element == 'file_uploaded':
log.debug('Blocked a File upload (%d > %d)' % (GLSetting.anomalies_counter[
    element], alarm_level[element]))
log.debug('Blocked an Unknown event (=%s) !? [BUG!] (%d > %d)' % (element,
    GLSetting.anomalies_counter[element], alarm_level[element]))
