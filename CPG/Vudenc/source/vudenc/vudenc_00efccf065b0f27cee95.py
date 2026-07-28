def download():...
"""docstring"""
description = 'Select the leagues parameter from the following leagues:\n\n'
for league_id, league_name in LEAGUES_MAPPING.items():
description += '{} ({})\n'.format(league_id, league_name)
parser = ArgumentParser(description=description, formatter_class=
    RawDescriptionHelpFormatter)
parser.add_argument('leagues', nargs='*', default=['all'], help=
    'One of all or any league ids from above.')
args = parser.parse_args()
leagues = args.leagues
if len(leagues) == 1 and leagues[0] == 'all':
leagues = leagues[0]
for ind, func in enumerate([create_spi_tables, create_fd_tables,
func(leagues) if ind in (0, 1) else func()
