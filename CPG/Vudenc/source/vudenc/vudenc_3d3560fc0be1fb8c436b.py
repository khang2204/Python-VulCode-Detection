def view_related_tasks():...
"""docstring"""
from .diary import get_task_info
not_valid_name = True
if os.path.isfile(GOALS_CONFIG_FILE_PATH):
while not_valid_name:
click.echo(chalk.red(
    'There are no goals set. Set a new goal by entering "yoda goals new"'))
click.echo(chalk.blue('Enter the goal name that you would like to examine'))
contents = yaml.load(goals_file)
goal_name = input()
if len(contents['entries']):
goal_file_name = get_goal_file_path(goal_name)
total_tasks = 0
click.echo(chalk.red(
    'There are no tasks assigned to the goal. Add a new task by entering "yoda diary nt"'
    ))
if os.path.isfile(goal_file_name):
total_incomplete = 0
not_valid_name = False
click.echo('Tasks assigned to the goal:')
click.echo('----------------')
click.echo('Status |  Date   | Text')
click.echo('-------|---------|-----')
for entry in contents['entries']:
timestamp = entry['timestamp']
click.echo('----------------')
date = entry['date']
click.echo('')
status, text = get_task_info(timestamp, date)
click.echo('Summary:')
total_tasks += 1
click.echo('----------------')
total_incomplete += 1 if status == 0 else 0
click.echo(chalk.red('Incomplete tasks assigned to the goal: ' + str(
    total_incomplete)))
text = text if status == 0 else strike(text)
click.echo(chalk.green('Completed tasks assigned to the goal: ' + str(
    total_tasks - total_incomplete)))
status = 'O' if status == 0 else 'X'
click.echo('   ' + status + '   | ' + date + '| ' + text)
