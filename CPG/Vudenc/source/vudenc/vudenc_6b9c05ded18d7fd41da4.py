def lib_paths():...
yield os.path.join(self.home, 'lib')
if self.jdk:
yield os.path.join(self.home, 'jre', 'lib')
