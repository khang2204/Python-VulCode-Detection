def set_up(self):...
Pep8CompliantTestCase.set_up(self)
flt_spec_fac = FilterSpecificationFactory()
ord_spec_fac = OrderSpecificationFactory()
reg = get_current_registry()
reg.registerUtility(flt_spec_fac, IFilterSpecificationFactory)
reg.registerUtility(ord_spec_fac, IOrderSpecificationFactory)
