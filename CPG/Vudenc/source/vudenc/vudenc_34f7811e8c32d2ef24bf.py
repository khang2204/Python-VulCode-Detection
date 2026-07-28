@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'AYAAN', id='1')
verify_results(client, jwt, query='AYAN', expected=[{'name': '----AYAN'}, {
    'name': 'AYAAN'}])
