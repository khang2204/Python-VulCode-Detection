def padResults(results, start=0, **kw):...
if start:
results[0:0] = [None] * start
found = int(results.numFound)
tail = found - len(results)
results.extend([None] * tail)
