def install_prerequisites(self):...
_load_modules()
import yaml
self.app_id = yaml.load(open(os.path.join(self.base_dir, 'app.yaml'), 'r'))[
    'application']
logging.debug('Instance app id: %s' % self.app_id)
assert self.app_id
