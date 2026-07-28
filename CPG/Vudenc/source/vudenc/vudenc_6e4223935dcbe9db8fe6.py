@staticmethod...
from rasterio.features import rasterize
geom = df.geometry
out = rasterize(((g, value) for g in geom), out_shape=out_shape, transform=
    out_transform, fill=background_value)
return out
