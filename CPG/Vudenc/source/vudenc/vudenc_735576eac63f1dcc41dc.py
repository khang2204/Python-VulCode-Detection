def _get_static_folder():...
static_folder = os.path.abspath(os.path.join(os.path.abspath(__file__),
    '..', '..', '..', 'web-ui', 'app'))
if not os.path.exists(static_folder):
static_folder = os.path.abspath(os.path.join(os.path.abspath(__file__),
    '..', '..', '..', '..', 'web-ui', 'app'))
if not os.path.exists(static_folder):
static_folder = os.path.join('/', 'usr', 'share', 'pixelated-user-agent')
return static_folder
