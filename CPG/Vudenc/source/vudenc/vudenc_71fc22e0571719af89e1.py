@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'JASMINE', id='1')
verify_results(client, jwt, query='OSMOND', expected=[{'name': '----OSMOND'}])
