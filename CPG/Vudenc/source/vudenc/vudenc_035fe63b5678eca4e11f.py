@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'WREN', id='1')
verify_results(client, jwt, query='REN', expected=[{'name': '----REN'}, {
    'name': 'WREN'}])
