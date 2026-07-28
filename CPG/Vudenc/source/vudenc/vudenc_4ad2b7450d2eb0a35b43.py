@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'KRYSTAL', id='1')
verify_results(client, jwt, query='CHRISTAL', expected=[{'name':
    '----CHRISTAL'}, {'name': 'KRYSTAL'}])
