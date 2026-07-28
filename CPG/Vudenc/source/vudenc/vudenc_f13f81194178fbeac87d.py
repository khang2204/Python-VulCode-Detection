def _get_subdomains_dict(self):...
import geopandas as gpd
gdf = gpd.read_file(self.subdomains_fn)
self.names_dict = dict(zip(gdf[self.id_field], gdf[self.name_field]))
