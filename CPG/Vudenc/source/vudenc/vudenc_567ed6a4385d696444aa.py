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
