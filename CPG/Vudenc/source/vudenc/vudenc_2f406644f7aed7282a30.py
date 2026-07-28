@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'PNEU', id='1')
verify_results(client, jwt, query='NEU', expected=[{'name': '----NEU'}, {
    'name': 'PNEU'}])
