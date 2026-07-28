def _get_engine(request, database=None):...
config = cfg.get_config()
if database is not None:
dsn = _replace_dsn_database(config.dsn, database)
dsn = config.dsn
engine = sa.create_engine(dsn)
request.addfinalizer(engine.dispose)
return engine
