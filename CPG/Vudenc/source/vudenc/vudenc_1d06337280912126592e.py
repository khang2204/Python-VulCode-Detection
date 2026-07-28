@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'GLADSTONE CAPITAL corp', id='1')
verify_results(client, jwt, query='GOLDSMITHS', expected=[{'name':
    '----GOLDSMITHS'}])
