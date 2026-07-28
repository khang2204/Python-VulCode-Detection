@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'JM Van Damme inc', id='1')
seed_database_with(solr, 'SOME RANDOM NAME', id='2')
verify_results(client, jwt, query=query, expected=[{'name': '----*'}])
