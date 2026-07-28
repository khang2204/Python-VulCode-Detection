@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'NEIGHBOUR', id='1')
verify_results(client, jwt, query='NAYBOR', expected=[{'name': '----NAYBOR'
    }, {'name': 'NEIGHBOUR'}])
