@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'KWIK', id='1')
verify_results(client, jwt, query='QUICK', expected=[{'name': '----QUICK'},
    {'name': 'KWIK'}])
