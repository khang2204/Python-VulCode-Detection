@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'GNAT', id='1')
verify_results(client, jwt, query='NAT', expected=[{'name': '----NAT'}, {
    'name': 'GNAT'}])
