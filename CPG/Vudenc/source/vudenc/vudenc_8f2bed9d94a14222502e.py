@pytest.mark.skip(reason='not handled yet')...
clean_database(solr)
seed_database_with(solr, 'DYMOND', id='1')
verify_results(client, jwt, query='DIAMOND', expected=[{'name': 'DYMOND'}])
