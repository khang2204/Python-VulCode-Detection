def _replace_dsn_database(dsn, new_database):...
parsed = urlparse.urlparse(dsn)
replaced = parsed._replace(path=new_database)
return replaced.geturl()
