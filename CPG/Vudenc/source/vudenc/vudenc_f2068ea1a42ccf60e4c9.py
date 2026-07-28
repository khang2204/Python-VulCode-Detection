def create_names_mapping_table():...
"""docstring"""
left_data = pd.read_sql('select date, league, team1, team2 from spi_historical'
    , DB_CONNECTION)
right_data = pd.read_sql(
    'select Date, Div, HomeTeam, AwayTeam from fd_historical', DB_CONNECTION)
key_columns = ['key0', 'key1']
left_data.columns = key_columns + ['left_team1', 'left_team2']
right_data.columns = key_columns + ['right_team1', 'right_team2']
names_combinations = pd.merge(left_data, right_data, how='outer').dropna(
    ).drop(columns=key_columns).reset_index(drop=True)
similarity = names_combinations.apply(lambda row: SequenceMatcher(None, row
    .left_team1, row.right_team1).ratio() * SequenceMatcher(None, row.
    left_team2, row.right_team2).ratio(), axis=1)
names_combinations_similarity = pd.concat([names_combinations, similarity],
    axis=1)
indices = names_combinations_similarity.groupby(['left_team1', 'left_team2'])[0
    ].idxmax().values
names_matching = names_combinations.take(indices)
matching1 = names_matching.loc[:, (['left_team1', 'right_team1'])].rename(
    columns={'left_team1': 'left_team', 'right_team1': 'right_team'})
matching2 = names_matching.loc[:, (['left_team2', 'right_team2'])].rename(
    columns={'left_team2': 'left_team', 'right_team2': 'right_team'})
matching = matching1.append(matching2)
matching = matching.groupby(matching.columns.tolist()).size().reset_index()
indices = matching.groupby('left_team')[0].idxmax().values
names_mapping = matching.take(indices).drop(columns=0).reset_index(drop=True)
names_mapping.to_sql('names_mapping', DB_CONNECTION, index=False, if_exists
    ='replace')
