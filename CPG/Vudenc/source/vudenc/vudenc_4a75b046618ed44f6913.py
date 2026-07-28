def check_sub_command(c):...
"""docstring"""
sub_commands = {'new': new_goal, 'tasks': view_related_tasks, 'view':
    list_goals, 'complete': complete_goal, 'analyze': goals_analysis}
return sub_commands[c]()
click.echo(chalk.red('Command does not exist!'))
click.echo('Try "yoda goals --help" for more info')
