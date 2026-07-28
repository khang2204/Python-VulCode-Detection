def prepare(self):...
path_until_wildcard = re.split(self.dynamic_fill, self.file)[0]
dir = os.path.dirname(path_until_wildcard)
if len(dir) > 0 and not os.path.exists(dir):
os.makedirs(dir)
if e.errno != 17:
