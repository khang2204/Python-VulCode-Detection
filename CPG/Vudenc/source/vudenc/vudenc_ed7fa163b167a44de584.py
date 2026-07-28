def test_client_connect_refused(self):...
"""docstring"""
cli = Client()
environ_save = os.environ['PHOBOS_DSS_connect_string']
os.environ['PHOBOS_DSS_connect_string'
    ] = "dbname='tata', user='titi', password='toto'"
self.assertRaises(EnvironmentError, cli.connect)
os.environ['PHOBOS_DSS_connect_string'] = environ_save
