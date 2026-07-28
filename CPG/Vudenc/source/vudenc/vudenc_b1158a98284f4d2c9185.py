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
