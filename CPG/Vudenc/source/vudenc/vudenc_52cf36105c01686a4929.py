def initialize(self, is_api=True):...
self.is_api = is_api
self.assets = Environment(os.path.join(os.path.dirname(__file__),
    '../static'), '/static')
css_all = Bundle('css/bootstrap.min.css', 'css/material.min.css', Bundle(
    'css/schoolcms.css', 'css/dropdown.css', filters='cssmin'),
    'outdatedbrowser/outdatedbrowser.min.css', output='dict/plugin.min.css')
js_all = Bundle(Bundle('outdatedbrowser/outdatedbrowser.min.js',
    'react-0.13.2/react-with-addons.min.js', 'js/jquery-2.1.3.min.js',
    'js/bootstrap.min.js', 'js/react-bootstrap.min.js',
    'js/react-mini-router.min.js', 'js/marked.min.js', 'js/material.min.js',
    'js/isMobile.min.js', 'js/moment-with-locales.min.js', 'js/dropdown.js',
    filters='jsmin'), Bundle('schoolcms/init.jsx', 'schoolcms/mixin/*.jsx',
    'schoolcms/component/*.jsx', 'schoolcms/page/*.jsx', filters=('react',
    'jsmin')), output='dict/plugin.min.js')
self.assets.register('css_all', css_all)
self.assets.register('js_all', js_all)
