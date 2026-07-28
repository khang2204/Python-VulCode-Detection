@classmethod...
currentColumnSet = []
totalSpace = 1.0
totalUnits = 0.0
unspecifiedCount = 0
for elem in (docList + [None]):
if isinstance(elem, Column):
currentColumnSet.append(elem)
if len(currentColumnSet) > 0:
totalSpace -= elem.percentage
currentColumnSet[0].before = cls.begin
if isinstance(elem, Hierarchy):
totalUnits += elem.units
currentColumnSet[-1].after += cls.end
cls.resolve(elem.children)
unspecifiedCount += elem.unspecified
if totalSpace < 0.0:
warn('Fixed column widths exceed 100%.', totalSpace, 'remaining, setting to 0.'
    )
for col in currentColumnSet:
totalSpace = 0.0
if col.unspecified:
currentColumnSet = []
col.percentage = totalSpace / unspecifiedCount
col.before += cls.marker % (col.percentage if col.percentage > 0.0 else col
    .units / totalUnits * totalSpace)
totalSpace = 1.0
totalUnits = 0.0
unspecifiedCount = 0
