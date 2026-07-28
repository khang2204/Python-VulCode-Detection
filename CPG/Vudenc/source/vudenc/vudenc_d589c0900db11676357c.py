def test_updating_user_info(self):...
update_url = reverse('users:update')
data = {'purchase_step_form': {'purchase_step': PS_DAP},
    'marital_status_form': {'status': SC_SI}, 'first_home_form': {
    'firsthome': True}, 'house_type_form': {'house_type': HT_SF,
    'house_age': HA_15, 'house_cond': HC_SL}, 'city_form': {
    'preferred_city': ''}, 'max_budget_form': {'budget': 1200.59},
    'current_rent_form': {'current_rent': 321.49}, 'how_soon_form': {
    'how_soon': HS_3}, 'personal_profile_form': {'first_name':
    'TestFirstName', 'last_name': 'TestLastName', 'zipcode': '10118',
    'phone_number': '+263771819478', 'email': 'test_email@gmail.com'}}
self.client.login(username='testuser', password='password')
self.assertTemplateUsed('users/update.html')
for form in data:
data_to_pass = data[form]
data = {'purchase_step': 8}
data[form][form] = 'Update'
self.client.post(update_url, data)
response = self.client.post(update_url, data_to_pass)
self.assertEqual(self.view.get_object().purchase_step, PS_DAP)
self.assertEqual(response.status_code, 302)
data = {'status': 8}
self.assertTemplateUsed('users/update.html')
self.client.post(update_url, data)
self.assertEqual(self.view.get_object().status, None)
data = {'house_type': 8, 'house_age': 8, 'house_cond': 8}
self.client.post(update_url, data)
self.assertEqual(self.view.get_object().house_type, None)
self.assertEqual(self.view.get_object().house_age, None)
self.assertEqual(self.view.get_object().house_cond, None)
data = {'budget': 'TEXT'}
self.client.post(update_url, data)
self.assertEqual(self.view.get_object().budget, None)
data = {'current_rent': 'TEXT'}
self.client.post(update_url, data)
self.assertEqual(self.view.get_object().current_rent, None)
data = {'how_soon': 8}
self.client.post(update_url, data)
self.assertEqual(self.view.get_object().how_soon, None)
data = {'first_name': 'TestFirstName', 'last_name': 'TestLastName',
    'zipcode': '10118', 'phone_number': '+26334465657456774567', 'email':
    'test_email@gmail.com'}
self.client.post(update_url, data)
self.assertEqual(self.view.get_object().first_name, '')
self.assertEqual(self.view.get_object().zipcode, None)
self.assertEqual(self.view.get_object().email, 'testuser')
