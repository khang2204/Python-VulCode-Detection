def singleImage(dims, files=None, file=None, implicitDims='width=\\textwidth'):...
if not file:
file = files[0][0]
if dims[0]:
if dims[1]:
if dims[1]:
return self.markers[0] % (dims[0][0], dims[0][1], dims[1][0], dims[1][1], file)
return self.markers[1] % (dims[0][0], dims[0][1], file)
return self.markers[2] % (dims[1][0], dims[1][1], file)
return self.markers[3] % (implicitDims, file)
