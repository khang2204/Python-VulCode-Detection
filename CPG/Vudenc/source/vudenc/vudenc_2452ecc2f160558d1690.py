def get_routes():...
return [webapp2.Route('/', handler=RootHandler), webapp2.Route('/catalog',
    handler=CatalogHandler), webapp2.Route('/catalog/<machine_id>', handler
    =CatalogHandler), webapp2.Route('/leases', handler=LeaseRequestHandler),
    webapp2.Route('/leases/<lease_id>', handler=LeaseRequestHandler)]
