def make_eb_config(application_name, default_region):...
UTILS_DIR = os.path.dirname(os.path.abspath(__file__))
j2_env = Environment(loader=FileSystemLoader(UTILS_DIR))
return j2_env.get_template('templates/eb/config.yml').render(APPLICATION_NAME
    =application_name, DEFAULT_REGION=default_region)
