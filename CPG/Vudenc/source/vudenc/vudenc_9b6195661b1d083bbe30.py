@require_GET...
"""docstring"""
internal_parameters = ['app_form', 'format']
parameters = strip_parameters(request.GET, internal_parameters)
q_app_form = request.GET.get('app_form')
q_format = request.GET.get('format')
if not q_format:
q_format = 'p'
if not q_app_form:
return HttpResponse('Unrecognizable app_form')
q_app, q_form = q_app_form.split('.')[0], q_app_form.split('.')[1]
exec('from tcms.%s.forms import %s as form' % (q_app, q_form))
__import__('tcms.%s.forms' % q_app)
q_app_module = sys.modules['tcms.%s.forms' % q_app]
form_class = getattr(q_app_module, q_form)
form_params = form_class(initial=parameters)
html = getattr(form_params, 'as_' + q_format)
return HttpResponse(html())
