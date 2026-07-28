def complete_goal():...
"""docstring"""
not_valid_goal_number = 1
if os.path.isfile(GOALS_CONFIG_FILE_PATH):
contents = yaml.load(todays_tasks_entry)
click.echo(chalk.red(
    'There are no goals set. Set a new goal by entering "yoda goals new"'))
i = 0
no_goal_left = True
for entry in contents['entries']:
i += 1
if no_goal_left:
if entry['status'] == 0:
click.echo(chalk.green(
    'All goals have been completed! Add a new goal by entering "yoda goals new"'
    ))
click.echo('Goals:')
no_goal_left = False
click.echo('----------------')
click.echo('Number |  Deadline   | Goal')
click.echo('-------|-------------|-----')
i = 0
for entry in contents['entries']:
i += 1
while not_valid_goal_number:
deadline = entry['deadline']
click.echo(chalk.blue(
    'Enter the goal number that you would like to set as completed'))
text = entry['text'] if entry['status'] == 0 else strike(entry['text'])
goal_to_be_completed = int(input())
if entry['status'] == 0:
if goal_to_be_completed > len(contents['entries']):
click.echo('   ' + str(i) + '   | ' + deadline + '  | ' + text)
click.echo(chalk.red('Please Enter a valid goal number!'))
contents['entries'][goal_to_be_completed - 1]['status'] = 1
input_data(contents, GOALS_CONFIG_FILE_PATH)
not_valid_goal_number = 0
