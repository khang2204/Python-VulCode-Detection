def generate_ansible_playbook_from_template(self, template_file, data):...
templateLoader = jinja2.FileSystemLoader(searchpath='/')
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template(template_file)
outputText = template.render(data)
return outputText
