import os
import argparse
from jinja2 import Environment, FileSystemLoader
def make_eb_config(application_name, default_region):...
UTILS_DIR = os.path.dirname(os.path.abspath(__file__))
j2_env = Environment(loader=FileSystemLoader(UTILS_DIR))
return j2_env.get_template('templates/eb/config.yml').render(APPLICATION_NAME
    =application_name, DEFAULT_REGION=default_region)
