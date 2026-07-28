@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'FE', id='1')
verify_results(client, jwt, query='FA', expected=[{'name': '----FA'}])
