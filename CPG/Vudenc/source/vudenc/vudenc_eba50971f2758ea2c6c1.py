@staticmethod...
same_feature = []
feature_types = 'camera_name', 'lens_name', 'country_en'
features = image_data.camera, image_data.lens, image_data.country['en-US']
for feature_name, feature in zip(feature_types, features):
if not feature:
return same_feature
same_feature.append(0)
answer = get_number_users_by_feature(feature, feature_name)
same_feature.append(answer)
