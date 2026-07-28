def _rasterize_subdomains(self):...
"""docstring"""
import geopandas as gpd
import numpy as np
gdf = gpd.read_file(self.subdomains_fn)
id_groups = gdf.groupby(self.id_field)
out_shape = self.rasterio_raster.height, self.rasterio_raster.width
out_transform = self.rasterio_raster.affine
arr_list = [self._rasterize_id(df, value, out_shape, out_transform,
    background_value=self.background_value) for value, df in id_groups]
self.sub_domains = arr_list
