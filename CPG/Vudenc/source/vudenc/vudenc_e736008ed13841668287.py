def test_group_type_facet(self):...
response = self.c.get('/find/?q=diatom')
self.assertContains(response, 'Filter by Group Type')
response = self.c.get('/find/?q=diatom&group_type=Unidentified')
self.assertContains(response, 'Showing 1 - 20 of')
response = self.c.get('/find/?q=diatom&group_type=BadGroupName')
self.assertContains(response, 'Sorry, no result found')
