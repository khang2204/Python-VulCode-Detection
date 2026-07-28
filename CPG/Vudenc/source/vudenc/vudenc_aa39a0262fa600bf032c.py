@property...
for java_dist_dir in self._java_dist_dirs:
if os.path.isdir(java_dist_dir):
for path in os.listdir(java_dist_dir):
home = os.path.join(java_dist_dir, path)
if os.path.isdir(home):
yield self.Location.from_home(home)
