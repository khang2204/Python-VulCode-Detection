def prepare_answer(self):...
"""docstring"""
image_data = self.get_info()
self.save_info_to_db(image_data)
answer = ''
coordinates = image_data.latitude, image_data.longitude
if not coordinates[0]:
answer += messages[self.user.language]['no_gps']
answ_template = messages[self.user.language]['camera_info']
basic_data = (image_data.date_time, image_data.camera, image_data.lens,
    image_data.address[self.user.language])
for arg in zip(answ_template, basic_data):
if arg[1]:
lang = self.user.language
answer += f'*{arg[0]}*: {arg[1]}\n'
lang_templates = messages[lang]['users with the same feature'].values()
ppl_wth_same_featrs = self.find_num_users_with_same_feature(image_data)
for template, feature in zip(lang_templates, ppl_wth_same_featrs):
if feature:
return coordinates, answer
answer += f'{template} {feature}\n'
