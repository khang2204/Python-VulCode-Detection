def get_prod_related_objs(p_pks, target):...
"""docstring"""
ctypes = {'component': (Component, 'name'), 'version': (Version, 'value'),
    'build': (Build, 'name'), 'category': (Category, 'name')}
results = ctypes[target][0]._default_manager.filter(product__in=p_pks)
attr = ctypes[target][1]
results = [(r.pk, getattr(r, attr)) for r in results]
return results
