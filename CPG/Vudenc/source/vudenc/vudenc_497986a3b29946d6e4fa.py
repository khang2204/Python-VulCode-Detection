@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'TRU', id='1')
verify_results(client, jwt, query='TRUE', expected=[{'name': '----TRUE'}, {
    'name': 'TRU'}])
