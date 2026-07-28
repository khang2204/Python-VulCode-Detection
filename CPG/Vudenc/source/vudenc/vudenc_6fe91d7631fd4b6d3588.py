@app.route('/run/form/init', methods=['POST'])...
run_form = get_run_form()
commands = json.loads(request.data)['commands']
set_form_defaults(run_form, commands)
return json.dumps({'commands': commands, 'html': render_template(
    'run_form.html', form=run_form)})
