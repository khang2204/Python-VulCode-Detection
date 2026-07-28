@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'MCGREGOR', id='1')
verify_results(client, jwt, query='MACGREGOR', expected=[{'name':
    '----MACGREGOR'}, {'name': 'MCGREGOR'}])
