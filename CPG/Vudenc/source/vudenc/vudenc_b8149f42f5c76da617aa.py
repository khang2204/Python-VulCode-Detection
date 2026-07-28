@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'VENIZIA', id='1')
seed_database_with(solr, 'VENEZIA', id='2')
seed_database_with(solr, 'VANSEA', id='3')
seed_database_with(solr, 'WENSO', id='4')
verify_results(client, jwt, query='VENIZIA', expected=[{'name':
    '----VENIZIA'}, {'name': 'VENEZIA'}])
