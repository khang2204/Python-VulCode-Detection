@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'PLANCK', id='1')
verify_results(client, jwt, query='PLANK', expected=[{'name': '----PLANK'},
    {'name': 'PLANCK'}])
