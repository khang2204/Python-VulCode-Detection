def get_info(self):...
"""docstring"""
user_photo = self.open_photo(self.message)
image = self.image_handler(self.user, user_photo)
return image.get_image_info()
