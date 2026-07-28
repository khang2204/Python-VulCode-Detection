@pytest.mark.skip(reason='Rhyming not implemented yet')...
clean_database(solr)
seed_database_with(solr, 'GAYLEDESIGNS INC.', id='1')
seed_database_with(solr, 'GOLDSTREAM ELECTRICAL CORP', id='2')
seed_database_with(solr, 'GLADSTONE JEWELLERY LTD', id='3')
seed_database_with(solr, 'GOLDSTEIN HOLDINGS INC.', id='4')
seed_database_with(solr, 'CLOUDSIDE INN INCORPORATED', id='5')
seed_database_with(solr, 'GOLDSPRING PROPERTIES LTD', id='6')
seed_database_with(solr, 'GOLDSTRIPES AVIATION INC', id='7')
seed_database_with(solr, 'GLADSTONE CAPITAL CORP', id='8')
seed_database_with(solr, 'KLETAS LAW CORPORATION', id='9')
seed_database_with(solr, 'COLDSTREAM VENTURES INC.', id='10')
seed_database_with(solr, 'BLABLA ANYTHING', id='11')
verify_results(client, jwt, query='GOLDSMITHS', expected=[{'name':
    '----GOLDSMITHS'}, {'name': 'COLDSTREAM VENTURES INC.'}, {'name':
    'GOLDSPRING PROPERTIES LTD'}, {'name': 'GOLDSTEIN HOLDINGS INC.'}, {
    'name': 'GOLDSTREAM ELECTRICAL CORP'}, {'name':
    'GOLDSTRIPES AVIATION INC'}])
