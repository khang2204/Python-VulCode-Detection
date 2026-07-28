@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'AILEEN ENTERPRISES', id='1')
verify_results(client, jwt, query='ALAN HARGREAVES CORPORATION', expected=[
    {'name': '----ALAN HARGREAVES'}, {'name': '----ALAN'}])
