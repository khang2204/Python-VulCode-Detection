def test_truth_table(self):...
build_train_set()
train_model(prob_thresh=prob_thresh)
match_query = """
                        SELECT 
                            df_dilfo.job_number,
                            df_dilfo.city,
                            df_dilfo.address,
                            df_dilfo.title,
                            df_dilfo.owner,
                            df_dilfo.contractor,
                            df_dilfo.engineer,
                            df_dilfo.receiver_email,
                            df_dilfo.cc_email,
                            df_dilfo.quality,
                            df_matched.dcn_key,
                            df_matched.ground_truth
                        FROM 
                            df_dilfo 
                        LEFT JOIN 
                            df_matched
                        ON 
                            df_dilfo.job_number=df_matched.job_number
                        WHERE 
                            df_dilfo.closed=1
                        AND
                            df_matched.ground_truth=1
                        AND 
                            df_matched.validate=0
                    """
test_df_dilfo = pd.read_sql(match_query, conn)
test_web_df = scrape(ref=test_df_dilfo)
results = match(df_dilfo=test_df_dilfo, df_web=test_web_df, test=True,
    prob_thresh=prob_thresh, version='new')
qty_actual_matches = int(len(results) ** 0.5)
qty_found_matches = results[results.pred_match == 1].title.nunique()
self.assertTrue(qty_found_matches == qty_actual_matches, msg=
    f'qty_found_matches({qty_found_matches}) not equal qty_actual_matches({qty_actual_matches})'
    )
false_positives = len(results[results.pred_match == 1]) - qty_found_matches
self.assertTrue(false_positives <= round(qty_actual_matches * 0.25, 1), msg
    =
    f'found too many false positives ({false_positives}) out of total test projects ({qty_actual_matches})'
    )
sample_dilfo = pd.DataFrame({'job_number': '2387', 'city': 'Ottawa',
    'address': '2562 Del Zotto Ave., Ottawa, Ontario', 'title':
    'DWS Building Expansion', 'owner': 'Douglas Stalker', 'contractor':
    'GNC', 'engineer': 'Goodkey', 'receiver_email': 'alex.roy@dilfo.com',
    'cc_email': '', 'quality': '2', 'closed': '0'}, index=range(1))
sample_web = pd.DataFrame({'pub_date': '2019-03-06', 'city':
    'Ottawa-Carleton', 'address':
    '2562 Del Zotto Avenue, Gloucester, Ontario', 'title':
    'Construct a 1 storey storage addition to a 2 storey office/industrial building'
    , 'owner': 'Doug Stalker, DWS Roofing', 'contractor':
    'GNC Constructors Inc.', 'engineer': None, 'dcn_key':
    'B0046A36-3F1C-11E9-9A87-005056AA6F02'}, index=range(1))
is_match, prob = match(df_dilfo=sample_dilfo, df_web=sample_web, test=True,
    version='new').iloc[0][['pred_match', 'pred_prob']]
self.assertTrue(is_match, msg=
    f'Project #{sample_dilfo.job_number} did not match successfully. Match probability returned was {prob}.'
    )
results = match(df_dilfo=sample_dilfo, since='2019-03-05', until=
    '2019-03-07', test=True, version='new')
prob_from_db_cert = results[results.contractor == 'gnc'].iloc[0].pred_prob
self.assertTrue(round(prob, 2) == round(prob_from_db_cert, 2))
validate_model(prob_thresh=prob_thresh, test=True)
