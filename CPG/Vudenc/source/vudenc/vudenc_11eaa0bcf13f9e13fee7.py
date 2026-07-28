@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'KLASS', id='1')
verify_results(client, jwt, query='CLASS', expected=[{'name': '----CLASS'},
    {'name': 'KLASS'}])
