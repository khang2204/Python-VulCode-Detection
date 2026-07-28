@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'HELENAH WU & CO. INC.', id='1')
seed_database_with(solr, 'A BETTER WAY HERBALS LTD.', id='2')
verify_results(client, jwt, query='EH', expected=[{'name': '----EH'}])
