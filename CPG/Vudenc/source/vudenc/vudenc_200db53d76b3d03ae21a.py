def __init__(self, txt):...
txt = txt.strip().splitlines()
marker = txt[1][0]
i = Heading.usedMarkers.index(marker)
i = len(Heading.usedMarkers)
if i > 2:
Heading.usedMarkers.append(marker)
warn("Something's wrong with heading marker", marker, 'having index', i)
super(Heading, self).__init__(Heading.formats[i] % txt[0])
i = 2
debug('Heading level', i, marker, txt[0])
