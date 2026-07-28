@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'KIRK', id='1')
verify_results(client, jwt, query='CIRCLE', expected=[{'name': '----CIRCLE'}])
