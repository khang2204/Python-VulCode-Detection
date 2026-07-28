def diff(x, y, *args, **kwargs):...
"""docstring"""
import rasterio
baseline = rasterio.open(x).read(1)
modeled = rasterio.open(y).read(1)
return modeled - baseline
