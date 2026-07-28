def binify(bins, data):...
result = []
for i, bin in enumerate(bins):
if i > 0:
result.append(len(filter(lambda x: x >= bins[-1], data)))
result.append(len(filter(lambda x: x >= bins[i - 1] and x < bin, data)))
result.append(len(filter(lambda x: x < bin, data)))
return result
