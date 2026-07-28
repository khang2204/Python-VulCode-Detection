@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'RHEN GNAT', id='1')
verify_results(client, jwt, query='REN NAT', expected=[{'name':
    '----REN NAT'}, {'name': 'RHEN GNAT'}, {'name': '----REN'}])
