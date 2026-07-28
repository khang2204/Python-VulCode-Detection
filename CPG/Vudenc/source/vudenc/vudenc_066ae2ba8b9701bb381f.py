@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'FEEL', id='1')
verify_results(client, jwt, query='FILL', expected=[{'name': '----FILL'}])
