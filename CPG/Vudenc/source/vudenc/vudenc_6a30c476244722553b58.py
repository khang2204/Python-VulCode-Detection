def create_fd_tables(leagues_ids):...
"""docstring"""
base_url = 'http://www.football-data.co.uk'
cols = ['Date', 'Div', 'HomeTeam', 'AwayTeam']
features_cols = ['BbAvH', 'BbAvA', 'BbAvD', 'BbAv>2.5', 'BbAv<2.5', 'BbAHh',
    'BbAvAHH', 'BbAvAHA']
odds_cols = ['PSH', 'PSA', 'PSD', 'BbMx>2.5', 'BbMx<2.5', 'BbAHh',
    'BbMxAHH', 'BbMxAHA']
seasons = ['1617', '1718', '1819']
leagues_ids = check_leagues_ids(leagues_ids)
fd_historical = []
for league_id, season in product(leagues_ids, seasons):
data = pd.read_csv(join(base_url, 'mmz4281', season, league_id), usecols=
    cols + features_cols + odds_cols)
fd_historical = pd.concat(fd_historical, ignore_index=True)
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
fd_fixtures = pd.read_csv(join(base_url, 'fixtures.csv'), usecols=cols +
    features_cols + odds_cols)
data['season'] = season
fd_fixtures['Date'] = pd.to_datetime(fd_fixtures['Date'], dayfirst=True)
fd_historical.append(data)
fd_fixtures = fd_fixtures[fd_fixtures['Div'].isin(leagues_ids)]
for name, df in zip(['fd_historical', 'fd_fixtures'], [fd_historical,
df.to_sql(name, DB_CONNECTION, index=False, if_exists='replace')
