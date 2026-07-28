def create_spi_tables(leagues_ids):...
"""docstring"""
leagues_ids = check_leagues_ids(leagues_ids)
spi = pd.read_csv(
    'https://projects.fivethirtyeight.com/soccer-api/club/spi_matches.csv'
    ).drop(columns=['league_id'])
spi['date'] = pd.to_datetime(spi['date'], format='%Y-%m-%d')
leagues = [LEAGUES_MAPPING[league_id] for league_id in leagues_ids]
spi = spi[spi['league'].isin(leagues)]
inverse_leagues_mapping = {league: league_id for league_id, league in
    LEAGUES_MAPPING.items()}
spi['league'] = spi['league'].apply(lambda league: inverse_leagues_mapping[
    league])
mask = ~spi['score1'].isna() & ~spi['score2'].isna()
spi_historical, spi_fixtures = spi[mask], spi[~mask]
for name, df in zip(['spi_historical', 'spi_fixtures'], [spi_historical,
df.to_sql(name, DB_CONNECTION, index=False, if_exists='replace')
