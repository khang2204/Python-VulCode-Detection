@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'DOUBLE J AVIATION LTD.', id='1')
verify_results(client, jwt, query='TABLE', expected=[{'name': '----TABLE'}])
