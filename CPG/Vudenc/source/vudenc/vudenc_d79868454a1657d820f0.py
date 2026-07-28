def create_tables():...
config = cfg.get_config()
engine = sa.create_engine(config.dsn)
tables.Base.metadata.create_all(engine)
engine.dispose()
