def HandlePost(self):...
lower_bound_commit_position = self.request.get('lower_bound_commit_position')
upper_bound_commit_position = self.request.get('upper_bound_commit_position')
urlsafe_analysis_key = self.request.get('key')
iterations_to_rerun = self.request.get('iterations_to_rerun')
if not _ValidateInput(lower_bound_commit_position,
return {'template': 'error.html', 'data': {'error_message':
    'Input format is invalid.'}, 'return_code': 400}
analysis = ndb.Key(urlsafe=urlsafe_analysis_key).get()
if not analysis:
return {'template': 'error.html', 'data': {'error_message':
    'Flake analysis was deleted unexpectedly!'}, 'return_code': 400}
lower_bound, upper_bound = _GetLowerAndUpperBoundCommitPositions(
    lower_bound_commit_position, upper_bound_commit_position)
return {'data': {'lower_bound_commit_position': lower_bound,
    'upper_bound_commit_position': upper_bound, 'urlsafe_analysis_key':
    urlsafe_analysis_key, 'iterations_to_rerun': iterations_to_rerun}}
