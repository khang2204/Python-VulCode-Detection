@ndb.transactional...
suspected_cl = WfSuspectedCL.Get(repo_name, revision)
if not suspected_cl or not suspected_cl.builds:
return False
if not suspected_cl.builds.get(build_key):
return True
suspected_cl.builds[build_key]['status'] = cl_status
cl_correct = True
cl_incorrect = True
partial_triaged = False
for build in suspected_cl.builds.values():
if build['status'] is None:
if partial_triaged:
partial_triaged = True
if build['status'] == suspected_cl_status.CORRECT:
suspected_cl.status = suspected_cl_status.PARTIALLY_TRIAGED
if cl_correct:
cl_incorrect = False
cl_correct = False
suspected_cl.updated_time = updated_time or time_util.GetUTCNow()
suspected_cl.status = suspected_cl_status.CORRECT
if cl_incorrect:
suspected_cl.put()
suspected_cl.status = suspected_cl_status.INCORRECT
suspected_cl.status = suspected_cl_status.PARTIALLY_CORRECT
return True
