@property...
maybe_suffix = '' if self.version == 'custom' else '-synthetic'
return {'scalac': ['//:scalac{}'.format(maybe_suffix)], 'scala-library': [
    '//:scala-library{}'.format(maybe_suffix)]}
