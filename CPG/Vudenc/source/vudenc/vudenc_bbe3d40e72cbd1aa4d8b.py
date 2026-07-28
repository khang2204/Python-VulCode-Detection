@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'GHABLE', id='1')
verify_results(client, jwt, query='GABLE', expected=[{'name': '----GABLE'},
    {'name': 'GHABLE'}])
