def smartGrid(dims, files, implicitFillWidth=True):...
warn(
    'Image Frame: PIL support not yet implemented, falling back to basic grid. Some images may be distorted.'
    )
return grid(dims, files, implicitFillWidth)
