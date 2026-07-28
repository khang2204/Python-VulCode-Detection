@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'BEAR', id='1')
verify_results(client, jwt, query='BARE', expected=[{'name': '----BARE'}, {
    'name': 'BEAR'}])
