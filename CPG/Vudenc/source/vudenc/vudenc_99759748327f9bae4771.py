@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'EXTREME', id='1')
verify_results(client, jwt, query='XTREME', expected=[{'name': '----XTREME'
    }, {'name': 'EXTREME'}])
