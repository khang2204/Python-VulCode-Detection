from bottle import static_file
from streamline import NonIterableRouteBase
path = '/static/<path:path>'
def get_base_path(self):...
return self.config['runtime.static_dir']
