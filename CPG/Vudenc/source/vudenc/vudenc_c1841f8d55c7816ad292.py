@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'KOLDSMITHS', id='1')
verify_results(client, jwt, query='COLDSTREAM', expected=[{'name':
    '----COLDSTREAM'}, {'name': 'KOLDSMITHS'}])
