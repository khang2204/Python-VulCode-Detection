def __init__(self, subdomains_fn, rasterio_raster, id_field, name_field,...
"""docstring"""
import numpy as np
self.subdomains_fn = subdomains_fn
self.rasterio_raster = rasterio_raster
self.id_field = id_field
self.name_field = name_field
self.background_value = background_value
self._rasterize_subdomains()
self._get_subdomains_dict()
