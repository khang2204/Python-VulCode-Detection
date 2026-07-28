@pytest.mark.skip(reason='compound words not handled yet')...
clean_database(solr)
seed_database_with(solr, 'BEE KLEEN', id='1')
verify_results(client, jwt, query='BE-CLEAN', expected=[{'name': 'BEE KLEEN'}])
