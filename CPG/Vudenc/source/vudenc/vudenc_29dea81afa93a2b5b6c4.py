def get_run_form():...
run_form = RunForm()
run_form.exe_models.choices = get_models_choices()
return run_form
