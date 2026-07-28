@classmethod...
maxIndex = len(docList) - 1
if depth > 3:
warn('Nested lists to depth greater than 4')
for i, l in enumerate(docList):
depth = 3
if isinstance(l, cls):
if i == 0 or (docList[i - 1].kind != l.kind if isinstance(docList[i - 1],
if isinstance(l, Hierarchy):
l.before = cls.begins[l.kind] + l.before
if i == maxIndex or (docList[i + 1].kind != l.kind if isinstance(docList[i +
cls.resolve(l.children, depth)
if l.kind == 1 and not l.resume:
l.after += cls.ends[l.kind]
l.before %= cls.enumCounterCmd % (cls.enumCounters[depth], cls.
    counterValues[depth]) if l.resume else ''
cls.counterValues[depth] = 0
if l.kind == 1:
cls.counterValues[depth] += 1
cls.resolve(l.children, depth + 1)
