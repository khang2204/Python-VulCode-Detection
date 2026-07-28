def when_call_root_redirect(self):...
client = Client()
self.response = client.get(reverse('root-redirect'))
return self
