@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'AGGRI', id='1')
verify_results(client, jwt, query='AGRI', expected=[{'name': '----AGRI'}, {
    'name': 'AGGRI'}])
