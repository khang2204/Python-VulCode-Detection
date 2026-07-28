def test_habits_and_practices_cards(self):...
data = {'puc': ['2']}
response = self.client.post('/get_data/', data=data)
for hnp in [b'ball bearings', b'motorcycle', b'vitamin a&amp;d', b'dish soap']:
self.assertIn(hnp, response.content)
