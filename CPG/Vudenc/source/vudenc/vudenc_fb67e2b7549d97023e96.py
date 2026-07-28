"""Front-end UI."""
import logging
import os
import webapp2
from components import auth
from components import datastore_utils
from components import template
from components import utils
import handlers_endpoints
import models
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
"""Catalog handler."""
@auth.require(auth.is_admin)...
params = {'machines': [], 'next_page_token': None}
if machine_id:
machine = models.CatalogMachineEntry.get_by_id(machine_id)
query = models.CatalogMachineEntry.query().order(models.CatalogMachineEntry
    .dimensions.hostname)
if not machine:
page_token = self.request.get('page_token') or ''
self.abort(404)
params['machines'] = [machine]
params['machines'], params['next_page_token'] = datastore_utils.fetch_page(
    query, 50, page_token)
self.response.write(template.render('templates/catalog.html', params=params))
"""Lease request handler."""
@auth.require(auth.is_admin)...
params = {'lease_requests': [], 'next_page_token': None, 'now_ts': utils.
    time_time()}
if lease_id:
lease_request = models.LeaseRequest.get_by_id(lease_id)
query = models.LeaseRequest.query().order(-models.LeaseRequest.last_modified_ts
    )
if not lease_request:
page_token = self.request.get('page_token') or ''
self.abort(404)
params['lease_requests'] = [lease_request]
params['lease_requests'], params['next_page_token'
    ] = datastore_utils.fetch_page(query, 50, page_token)
self.response.write(template.render('templates/leases.html', params=params))
"""Root handler."""
@auth.public...
params = {'is_admin': auth.is_admin()}
self.response.write(template.render('templates/root.html', params=params))
def get_routes():...
return [webapp2.Route('/', handler=RootHandler), webapp2.Route('/catalog',
    handler=CatalogHandler), webapp2.Route('/catalog/<machine_id>', handler
    =CatalogHandler), webapp2.Route('/leases', handler=LeaseRequestHandler),
    webapp2.Route('/leases/<lease_id>', handler=LeaseRequestHandler)]
