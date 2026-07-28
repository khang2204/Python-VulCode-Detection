@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'ANDERSON BEHAVIOR CONSULTING INC.', id='1')
verify_results(client, jwt, query='BEHAVIOUR INTERVENTION', expected=[{
    'name': '----BEHAVIOUR INTERVENTION'}, {'name': '----BEHAVIOUR'}, {
    'name': 'ANDERSON BEHAVIOR CONSULTING INC.'}])
