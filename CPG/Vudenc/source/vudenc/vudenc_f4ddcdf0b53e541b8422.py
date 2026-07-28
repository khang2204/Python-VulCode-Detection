@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'FEY', id='1')
verify_results(client, jwt, query='FAY', expected=[{'name': '----FAY'}, {
    'name': 'FEY'}])
