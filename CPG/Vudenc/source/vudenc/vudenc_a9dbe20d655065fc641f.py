def _init_helper(self, arr):...
if len(arr) == 0:
warn('Skipping empty scissor command')
if not (os.path.isfile(arr[0]) or os.path.isfile(arr[0] + '.pdf')):
return ''
warn('File included in scissor command not found, proceeding unsafely...')
if len(arr) > 1:
if re.fullmatch('\\d+(-\\d+)?(,\\d+(-\\d+)?)*', arr[1]):
cmd = self.includeCmd % ''
cmd = self.includeCmd % self.pagesSpec
warn('Ignoring malformed page range in scissor command')
return cmd % arr[0]
return cmd % (arr[1], arr[0])
if len(arr) > 2:
warn('Ignoring extraneous arguments in scissor command')
