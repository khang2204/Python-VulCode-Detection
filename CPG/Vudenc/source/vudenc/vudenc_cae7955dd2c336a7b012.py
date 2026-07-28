@api.require(api.is_superuser)...
web_client_id = self.request.POST['web_client_id']
api.set_web_client_id(web_client_id)
self.show_page(web_client_id=web_client_id, saved=True)
