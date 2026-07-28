@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'BODY BLUEPRINT FITNESS INC.', id='1')
seed_database_with(solr, 'BLUEPRINT BEAUTEE', id='2')
verify_results(client, jwt, query='BLUEPRINT BEAUTY', expected=[{'name':
    '----BLUEPRINT BEAUTY'}, {'name': 'BLUEPRINT BEAUTEE'}, {'name':
    '----BLUEPRINT synonyms:(BEAUTI)'}])
