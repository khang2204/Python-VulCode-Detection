@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'GOLDSTREAM ELECTRICAL LTD')
verify_results(client, jwt, query='GOLDSMITHS', expected=[{'name':
    '----GOLDSMITHS'}, {'name': 'GOLDSTREAM ELECTRICAL LTD'}])
