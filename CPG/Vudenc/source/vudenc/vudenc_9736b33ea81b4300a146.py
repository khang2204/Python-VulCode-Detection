@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'LABORATORY', id='1')
seed_database_with(solr, 'LAPORTE', id='2')
seed_database_with(solr, 'LIBERTI', id='3')
verify_results(client, jwt, query='LIBERTY', expected=[{'name':
    '----LIBERTY'}, {'name': 'LIBERTI'}])
