@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'PHEEL', id='1')
verify_results(client, jwt, query='FEEL', expected=[{'name': '----FEEL'}, {
    'name': 'PHEEL'}])
