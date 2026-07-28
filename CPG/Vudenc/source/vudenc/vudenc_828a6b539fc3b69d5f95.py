@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'WHITE', id='1')
verify_results(client, jwt, query='WITE', expected=[{'name': '----WITE'}, {
    'name': 'WHITE'}])
