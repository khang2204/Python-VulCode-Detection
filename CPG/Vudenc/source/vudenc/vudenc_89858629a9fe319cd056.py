@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'CRYSTAL', id='1')
verify_results(client, jwt, query='CRISTAL', expected=[{'name':
    '----CRISTAL'}, {'name': 'CRYSTAL'}])
