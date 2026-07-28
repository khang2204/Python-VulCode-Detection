@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'CRAZY', id='1')
seed_database_with(solr, 'KAIZEN', id='2')
verify_results(client, jwt, query='CAYZEN', expected=[{'name': '----CAYZEN'
    }, {'name': 'KAIZEN'}])
