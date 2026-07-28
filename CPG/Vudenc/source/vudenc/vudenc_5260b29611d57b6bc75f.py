@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'OYSTER', id='1')
verify_results(client, jwt, query='OISTER', expected=[{'name': '----OISTER'
    }, {'name': 'OYSTER'}])
