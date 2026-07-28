@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'LEAK', id='1')
verify_results(client, jwt, query='LEEK', expected=[{'name': 'LEAK'}])
