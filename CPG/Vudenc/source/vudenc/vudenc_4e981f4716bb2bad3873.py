@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'KOFI', id='1')
verify_results(client, jwt, query='COFFI', expected=[{'name': '----COFFI'},
    {'name': 'KOFI'}])
