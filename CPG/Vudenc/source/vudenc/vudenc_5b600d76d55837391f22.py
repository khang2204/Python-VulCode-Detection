@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'FEDS', id='1')
verify_results(client, jwt, query='FADS', expected=[{'name': '----FADS'}])
