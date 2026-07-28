def render_template(template, config):...
if is_executable(template):
return render_executable(template, config)
return render_moustache(open(template).read(), config)
logger.error('%s', e)
