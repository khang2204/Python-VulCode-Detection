@app.route('/run/form/remove/<field>', methods=['POST'])...
run_form = get_run_form()
run_form[field].pop_entry()
commands = get_commands(run_form)
set_form_defaults(run_form, commands)
return json.dumps({'commands': commands, 'html': render_template(
    'run_form.html', form=run_form)})
