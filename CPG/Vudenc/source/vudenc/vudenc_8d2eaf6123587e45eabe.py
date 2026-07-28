def test_scarpe_to_communicate(self):...
test_limit = 3
web_df = scrape(limit=test_limit, test=True, since='week_ago')
self.assertEqual(len(web_df), test_limit)
match_first_query = 'SELECT * FROM df_dilfo WHERE closed=0 LIMIT 1'
dilfo_row = pd.read_sql(match_first_query, conn).iloc[0]
communicate(web_df, dilfo_row, test=True)
