def add_render_globals_to_template(event):...
request = event['request']
event['_'] = request.translate
event['localizer'] = request.localizer
event['h'] = template_helpers
