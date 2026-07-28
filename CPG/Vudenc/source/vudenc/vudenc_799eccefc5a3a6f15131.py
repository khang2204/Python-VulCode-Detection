def app(self):...
app = Sanic(__name__)
default_templates = str(app_root / 'datasette' / 'templates')
template_paths = []
if self.template_dir:
template_paths.append(self.template_dir)
template_paths.extend([plugin['templates_path'] for plugin in get_plugins(
    pm) if plugin['templates_path']])
template_paths.append(default_templates)
template_loader = ChoiceLoader([FileSystemLoader(template_paths),
    PrefixLoader({'default': FileSystemLoader(default_templates)},
    delimiter=':')])
self.jinja_env = Environment(loader=template_loader, autoescape=True)
self.jinja_env.filters['escape_css_string'] = escape_css_string
self.jinja_env.filters['quote_plus'] = lambda u: urllib.parse.quote_plus(u)
self.jinja_env.filters['escape_sqlite'] = escape_sqlite
self.jinja_env.filters['to_css_class'] = to_css_class
pm.hook.prepare_jinja2_environment(env=self.jinja_env)
app.add_route(IndexView.as_view(self), '/<as_format:(\\.jsono?)?$>')
app.add_route(favicon, '/favicon.ico')
app.static('/-/static/', str(app_root / 'datasette' / 'static'))
for path, dirname in self.static_mounts:
app.static(path, dirname)
for plugin in get_plugins(pm):
if plugin['static_path']:
app.add_route(JsonDataView.as_view(self, 'inspect.json', self.inspect),
    '/-/inspect<as_format:(\\.json)?$>')
modpath = '/-/static-plugins/{}/'.format(plugin['name'])
app.add_route(JsonDataView.as_view(self, 'metadata.json', lambda : self.
    _metadata), '/-/metadata<as_format:(\\.json)?$>')
app.static(modpath, plugin['static_path'])
app.add_route(JsonDataView.as_view(self, 'versions.json', self.versions),
    '/-/versions<as_format:(\\.json)?$>')
app.add_route(JsonDataView.as_view(self, 'plugins.json', self.plugins),
    '/-/plugins<as_format:(\\.json)?$>')
app.add_route(JsonDataView.as_view(self, 'config.json', lambda : self.
    _config), '/-/config<as_format:(\\.json)?$>')
app.add_route(DatabaseDownload.as_view(self),
    '/<db_name:[^/]+?><as_db:(\\.db)$>')
app.add_route(DatabaseView.as_view(self),
    '/<db_name:[^/]+?><as_format:(\\.jsono?|\\.csv)?$>')
app.add_route(TableView.as_view(self),
    '/<db_name:[^/]+>/<table_and_format:[^/]+?$>')
app.add_route(RowView.as_view(self),
    '/<db_name:[^/]+>/<table:[^/]+?>/<pk_path:[^/]+?><as_format:(\\.jsono?)?$>'
    )
self.register_custom_units()
@app.middleware('response')...
if original_response.status == 404 and request.path.endswith('/'):
path = request.path.rstrip('/')
@app.exception(Exception)...
if request.query_string:
title = None
path = '{}?{}'.format(path, request.query_string)
return response.redirect(path)
help = None
if isinstance(exception, NotFound):
status = 404
if isinstance(exception, InvalidUsage):
info = {}
status = 405
if isinstance(exception, DatasetteError):
message = exception.args[0]
info = {}
status = exception.status
status = 500
templates = ['500.html']
message = exception.args[0]
info = exception.error_dict
info = {}
if status != 500:
message = exception.message
message = str(exception)
templates = ['{}.html'.format(status)] + templates
info.update({'ok': False, 'error': message, 'status': status, 'title': title})
if exception.messagge_is_html:
traceback.print_exc()
if request is not None and request.path.split('?')[0].endswith('.json'):
message = Markup(message)
title = exception.title
return response.json(info, status=status)
template = self.jinja_env.select_template(templates)
return response.html(template.render(info), status=status)
