def _create_sqlite_engine(self, connection_url):...
engine = create_engine(connection_url, connect_args={'check_same_thread': 
    False}, poolclass=StaticPool)
return engine
