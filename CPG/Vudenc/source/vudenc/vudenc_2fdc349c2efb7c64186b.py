@pytest.mark.skip(reason='not handled yet')...
clean_database(solr)
seed_database_with(solr, 'TERRA', id='1')
verify_results(client, jwt, query='TARA', expected=[{'name': 'TERRA'}])
