@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'ACME', id='1')
verify_results(client, jwt, query='EQUIOM', expected=[{'name': '----EQUIOM'}])
