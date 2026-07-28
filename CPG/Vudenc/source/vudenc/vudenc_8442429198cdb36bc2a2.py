@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'LIBERTI', id='1')
verify_results(client, jwt, query='LIBERTY', expected=[{'name':
    '----LIBERTY'}, {'name': 'LIBERTI'}])
