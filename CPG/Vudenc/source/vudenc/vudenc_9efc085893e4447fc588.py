def get_app_dir():...
d = sys.path[0]
d = d.split('/')[-1]
return sys.path[0] if d == 'app' else os.path.dirname(sys.path[0])
