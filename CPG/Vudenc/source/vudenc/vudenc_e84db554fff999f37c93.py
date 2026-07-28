@app.route('/run/form/submit', methods=['POST'])...
run_form = get_run_form()
commands = get_commands(run_form)
if run_form.validate_on_submit():
return json.dumps({'commands': commands, 'html': render_template(
    'run_success.html', commands=commands)})
return json.dumps({'commands': commands, 'html': render_template(
    'run_form.html', form=run_form)}), 400
