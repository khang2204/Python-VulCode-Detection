def create_query_bounds_pad_fn(buffer_cfg, layer_name):...
if not buffer_cfg:
return _bounds_pad_no_buf
buf_by_type = dict(point=0, line=0, polygon=0)
for format_ext, format_cfg in buffer_cfg.items():
format_layer_cfg = format_cfg.get('layer', {}).get(layer_name)
if buf_by_type['point'] == buf_by_type['line'] == buf_by_type['polygon'] == 0:
format_geometry_cfg = format_cfg.get('geometry', {})
return _bounds_pad_no_buf
def bounds_pad(bounds, meters_per_pixel_dim):...
if format_layer_cfg:
buffered_by_type = {}
for geometry_type, buffer_size in format_layer_cfg.items():
if format_geometry_cfg:
for geometry_type in ('point', 'line', 'polygon'):
buf_by_type[geometry_type] = max(buf_by_type[geometry_type], buffer_size)
for geometry_type, buffer_size in format_geometry_cfg.items():
offset = meters_per_pixel_dim * buf_by_type[geometry_type]
return buffered_by_type
buf_by_type[geometry_type] = max(buf_by_type[geometry_type], buffer_size)
buffered_by_type[geometry_type] = bounds_buffer(bounds, offset)
