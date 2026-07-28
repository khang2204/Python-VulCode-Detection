def get_db(app, context):...
"""docstring"""
if not hasattr(context, 'db'):
dsn_tns = cx_Oracle.makedsn(app.config['DB_SERVER'], app.config['DB_PORT'],
    app.config['DB_SID'])
return context.db
context.db = cx_Oracle.connect(app.config['DB_USER'], app.config['DB_PWD'],
    dsn_tns)
