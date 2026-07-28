def after_step(context, step):...
if step.status == 'failed':
id = str(uuid.uuid4())
os.chdir('screenshots')
context.browser.save_screenshot('failed ' + str(step.name) + '_' + id + '.png')
save_source(context, 'failed ' + str(step.name) + '_' + id + '.html')
os.chdir('../')
