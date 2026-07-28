def __init__(self, filename):...
self.path = os.path.dirname(filename)
self.filename = os.path.basename(filename)
self.node_number = re.search('\\b\\d{14}\\b|$', filename).group(0)
self.index = re.search('^\\d{2}\\b|$', filename).group(0)
self.title = re.search('[^\\d]+|$', filename).group(0).strip()
self.log()
