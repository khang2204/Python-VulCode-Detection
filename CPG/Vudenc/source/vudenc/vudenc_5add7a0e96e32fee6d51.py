def write_eb_config(dest, application_name, default_region):...
contents = make_eb_config(application_name, default_region)
fh = open(dest, 'w')
fh.write(contents)
fh.close()
