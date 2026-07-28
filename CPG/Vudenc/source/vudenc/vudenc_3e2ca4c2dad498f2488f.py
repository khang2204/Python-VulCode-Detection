@app.after_request...
"""docstring"""
g.session.commit()
g.session.close()
return resp
