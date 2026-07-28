@integration_synonym_api...
clean_database(solr)
seed_database_with(solr, 'FINGER LIMATED', id='1')
verify_results(client, jwt, query='SUN LIMITED', expected=[{'name': '----SUN'}]
    )
