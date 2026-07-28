@app.before_request...
"""docstring"""
g.session = Session(engine)
g.Base = Base
