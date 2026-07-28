@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'PSYCHO', id='1')
verify_results(client, jwt, query='SYCHO', expected=[{'name': '----SYCHO'},
    {'name': 'PSYCHO'}])
