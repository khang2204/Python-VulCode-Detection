def goals_analysis():...
"""docstring"""
now = datetime.datetime.now()
total_goals = 0
total_incomplete_goals = 0
total_missed_goals = 0
total_goals_next_week = 0
total_goals_next_month = 0
if os.path.isfile(GOALS_CONFIG_FILE_PATH):
contents = yaml.load(goals_file)
click.echo(chalk.red(
    'There are no goals set. Set a new goal by entering "yoda goals new"'))
for entry in contents['entries']:
total_goals += 1
percent_incomplete_goals = total_incomplete_goals * 100 / total_goals
if entry['status'] == 0:
percent_complete_goals = 100 - percent_incomplete_goals
total_incomplete_goals += 1
click.echo(chalk.red('Percentage of incomplete goals : ' + str(
    percent_incomplete_goals)))
deadline = datetime.datetime.strptime(entry['deadline'], '%Y-%m-%d')
click.echo(chalk.green('Percentage of completed goals : ' + str(
    percent_complete_goals)))
total_missed_goals += 1 if deadline < now else 0
click.echo(chalk.blue('Number of missed deadlines : ' + str(
    total_missed_goals)))
total_goals_next_week += 1 if (deadline - now).days <= 7 else 0
click.echo(chalk.blue('Number of goals due within the next week : ' + str(
    total_goals_next_week)))
total_goals_next_month += 1 if (deadline - now).days <= 30 else 0
click.echo(chalk.blue('Number of goals due within the next month : ' + str(
    total_goals_next_month)))
