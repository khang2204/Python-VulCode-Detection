def bounds_pad(bounds, meters_per_pixel_dim):...
buffered_by_type = {}
for geometry_type in ('point', 'line', 'polygon'):
offset = meters_per_pixel_dim * buf_by_type[geometry_type]
return buffered_by_type
buffered_by_type[geometry_type] = bounds_buffer(bounds, offset)
