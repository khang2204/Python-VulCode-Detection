def create_empty_extra_products(self):...
if self.context.products.is_required_data('zinc_analysis'):
self.context.products.safe_create_data('zinc_analysis', dict)
if self.context.products.is_required_data('zinc_args'):
self.context.products.safe_create_data('zinc_args', lambda : defaultdict(list))
