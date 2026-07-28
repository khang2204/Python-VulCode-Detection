def test_get_form(self):...
response = self.client.get(reverse('ajax-form'), {'app_form':
    'testcases.CaseAutomatedForm'})
form = CaseAutomatedForm()
self.assertHTMLEqual(str(response.content, encoding=settings.
    DEFAULT_CHARSET), form.as_p())
