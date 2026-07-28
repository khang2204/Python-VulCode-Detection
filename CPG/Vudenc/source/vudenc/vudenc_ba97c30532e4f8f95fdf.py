@ndb.transactional...
analysis = WfAnalysis.Get(master_name, builder_name, build_number)
if not analysis or not analysis.suspected_cls:
return False
num_correct = 0
num_incorrect = 0
for cl in analysis.suspected_cls:
if cl['repo_name'] == repo_name and cl['revision'] == revision:
if num_correct + num_incorrect == len(analysis.suspected_cls):
cl['status'] = cl_status
if cl.get('status') == suspected_cl_status.CORRECT:
if num_correct == 0:
analysis.put()
num_correct += 1
if cl.get('status') == suspected_cl_status.INCORRECT:
analysis.result_status = result_status.FOUND_INCORRECT
if num_incorrect == 0:
return True
num_incorrect += 1
analysis.result_status = result_status.FOUND_CORRECT
analysis.result_status = result_status.PARTIALLY_CORRECT_FOUND
