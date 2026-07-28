def _GetLastAttemptedSwarmingTaskDetails(analysis):...
swarming_task_id = analysis.last_attempted_swarming_task_id
build_number = analysis.last_attempted_build_number
task_id = swarming_task_id if swarming_task_id and swarming_task_id.lower(
    ) not in (NO_TASK, NO_TASK_EXCEPTION) else None
return {'task_id': task_id, 'build_number': build_number}
