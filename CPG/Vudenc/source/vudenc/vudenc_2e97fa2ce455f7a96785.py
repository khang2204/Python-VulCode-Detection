def add_task_to_goal(goal_name, date, timestamp):...
goal_filename = get_goal_file_path(goal_name)
if os.path.isfile(goal_filename):
setup_data = dict(date=date, timestamp=timestamp)
return False
append_data_into_file(setup_data, goal_filename)
return True
