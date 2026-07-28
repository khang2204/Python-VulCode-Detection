@app.teardown_appcontext...
"""docstring"""
connection = getattr(g, 'database', None)
if connection is not None:
connection.close()
