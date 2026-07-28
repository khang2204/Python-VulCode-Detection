def update_filename(instance, filename):...
name_fill_space = instance.name.replace(' ', '_')
name = '{0}/{0}_{1}'.format(name_fill_space, filename)
return name
