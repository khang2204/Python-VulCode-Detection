def _ValidateInput(lower_bound_commit_position, upper_bound_commit_position,...
if lower_bound_commit_position is None and upper_bound_commit_position is None:
return False
if lower_bound_commit_position is not None:
return False
lower_bound_commit_position = int(lower_bound_commit_position)
if upper_bound_commit_position is not None:
upper_bound_commit_position = int(upper_bound_commit_position)
iterations_to_rerun = int(iterations_to_rerun)
return True
