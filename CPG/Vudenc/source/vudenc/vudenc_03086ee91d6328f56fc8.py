@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'ANDERSON BEHAVIOR CONSULTING', id='1')
verify_results(client, jwt, query='INTERVENTION BEHAVIOUR', expected=[{
    'name': '----INTERVENTION BEHAVIOUR'}, {'name': '----INTERVENTION'}])
