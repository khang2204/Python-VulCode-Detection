@classmethod...
super(TestUpdateObject, cls).setUpTestData()
cls.permission = 'testplans.change_testplan'
cls.update_url = reverse('ajax-update')
