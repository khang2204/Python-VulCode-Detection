def list_goals():...
"""docstring"""
if os.path.isfile(GOALS_CONFIG_FILE_PATH):
contents = yaml.load(goals_file)
click.echo(
    'There are no goals set. Set a new goal by entering "yoda goals new"')
if len(contents):
contents['entries'].sort(key=lambda x: x['deadline'].split('-'))
click.echo(
    'There are no goals set. Set a new goal by entering "yoda goals new"')
click.echo('Goals')
click.echo('----------------')
click.echo('Status |  Deadline   | Name: text')
click.echo('-------|-------------|---------------')
incomplete_goals = 0
total_tasks = 0
total_missed_deadline = 0
for entry in contents['entries']:
total_tasks += 1
click.echo('----------------')
incomplete_goals += 1 if entry['status'] == 0 else 0
click.echo('')
deadline = entry['deadline']
click.echo('Summary:')
name = entry['name']
click.echo('----------------')
text = entry['text'] if entry['status'] == 0 else strike(entry['text'])
if incomplete_goals == 0:
status = 'O' if entry['status'] == 0 else 'X'
click.echo(chalk.green(
    'All goals have been completed! Set a new goal by entering "yoda goals new"'
    ))
click.echo(chalk.red('Incomplete tasks: ' + str(incomplete_goals)))
deadline_time = datetime.datetime.strptime(deadline, '%Y-%m-%d')
click.echo(chalk.red('Tasks with missed deadline: ' + str(
    total_missed_deadline)))
now = datetime.datetime.now()
click.echo(chalk.green('Completed tasks: ' + str(total_tasks -
    incomplete_goals)))
total_missed_deadline += 1 if deadline_time < now else 0
click.echo('   ' + status + '   | ' + deadline + '  | #' + name + ': ' + text)
