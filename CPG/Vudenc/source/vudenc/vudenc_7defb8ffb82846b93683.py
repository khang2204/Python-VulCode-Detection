@pytest.fixture(scope='session', autouse=True)...
test_db_name = _get_test_db_name()
conn.execute(f'DROP DATABASE IF EXISTS {test_db_name}')
conn.execute(f'CREATE DATABASE {test_db_name}')
create_tables()
request.addfinalizer(lambda : _drop_database(_system_engine))
