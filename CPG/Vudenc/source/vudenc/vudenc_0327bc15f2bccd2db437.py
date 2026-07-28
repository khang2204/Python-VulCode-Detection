def create_modeling_tables():...
"""docstring"""
spi_keys = ['date', 'league', 'team1', 'team2']
fd_keys = ['Date', 'Div', 'HomeTeam', 'AwayTeam']
input_cols = ['spi1', 'spi2', 'prob1', 'prob2', 'probtie', 'proj_score1',
    'proj_score2', 'importance1', 'importance2', 'BbAvH', 'BbAvA', 'BbAvD',
    'BbAv>2.5', 'BbAv<2.5', 'BbAHh', 'BbAvAHH', 'BbAvAHA']
output_cols = ['score1', 'score2', 'xg1', 'xg2', 'nsxg1', 'nsxg2',
    'adj_score1', 'adj_score2']
odds_cols_mapping = {'PSH': 'H', 'PSA': 'A', 'PSD': 'D', 'BbMx>2.5':
    'over_2.5', 'BbMx<2.5': 'under_2.5', 'BbAHh': 'handicap', 'BbMxAHH':
    'handicap_home', 'BbMxAHA': 'handicap_away'}
data = {}
for name in ('spi_historical', 'spi_fixtures', 'fd_historical',
parse_dates = ['date'] if name in ('spi_historical', 'spi_fixtures') else [
    'Date'] if name in ('fd_historical', 'fd_fixtures') else None
for col in ['team1', 'team2']:
data[name] = pd.read_sql('select * from %s' % name, DB_CONNECTION,
    parse_dates=parse_dates)
for name in ('spi_historical', 'spi_fixtures'):
historical = pd.merge(data['spi_historical'], data['fd_historical'],
    left_on=spi_keys, right_on=fd_keys).dropna(subset=odds_cols_mapping.
    keys(), how='any').reset_index(drop=True)
data[name] = pd.merge(data[name], data['names_mapping'], left_on=col,
    right_on='left_team', how='left').drop(columns=[col, 'left_team']).rename(
    columns={'right_team': col})
fixtures = pd.merge(data['spi_fixtures'], data['fd_fixtures'], left_on=
    spi_keys, right_on=fd_keys)
X = historical.loc[:, (['season'] + spi_keys + input_cols)]
y = historical.loc[:, (output_cols)]
odds = historical.loc[:, (spi_keys + list(odds_cols_mapping.keys()))].rename(
    columns=odds_cols_mapping)
X_test = fixtures.loc[:, (spi_keys + input_cols)]
odds_test = fixtures.loc[:, (spi_keys + list(odds_cols_mapping.keys()))
    ].rename(columns=odds_cols_mapping)
for ind in (1, 2):
y['avg_score%s' % ind] = y[['score%s' % ind, 'xg%s' % ind, 'nsxg%s' % ind]
    ].mean(axis=1)
for target_type in TARGET_TYPES_MAPPING.keys():
if '+' in target_type:
for df in (X, X_test):
target_types = target_type.split('+')
df['quality'] = hmean(df[['spi1', 'spi2']], axis=1)
for name, df in zip(['X', 'y', 'odds', 'X_test', 'odds_test'], [X, y, odds,
odds = combine_odds(odds, target_types)
df['importance'] = df[['importance1', 'importance2']].mean(axis=1)
df.to_sql(name, DB_CONNECTION, index=False, if_exists='replace')
odds_test = combine_odds(odds_test, target_types)
df['rating'] = df[['quality', 'importance']].mean(axis=1)
df['sum_proj_score'] = df['proj_score1'] + df['proj_score2']
