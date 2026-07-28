def register_blueprints(app):...
"""docstring"""
for name in find_modules('benwaonline.blueprints'):
mod = import_string(name)
return None
if hasattr(mod, 'bp'):
app.register_blueprint(mod.bp)
