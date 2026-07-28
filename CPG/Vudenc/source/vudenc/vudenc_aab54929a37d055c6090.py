def get_image_database(type):...
image_databases = {'camera': camera_images_db, 'main': main_images_db}
if not type in image_databases:
return image_databases[type]
