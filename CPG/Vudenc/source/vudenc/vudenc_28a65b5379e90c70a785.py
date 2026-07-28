@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'ANDERSON BEHAVIOR BEHAVIOR', id='1')
verify_results(client, jwt, query='BEHAVIOUR INTERVENTION', expected=[{
    'name': '----BEHAVIOUR INTERVENTION'}, {'name': '----BEHAVIOUR'}, {
    'name': 'ANDERSON BEHAVIOR BEHAVIOR'}])
