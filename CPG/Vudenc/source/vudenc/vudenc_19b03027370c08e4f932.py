def save_info_to_db(self, image_data):...
"""docstring"""
camera_name, lens_name = image_data.camera, image_data.lens
camera_name = f'"{camera_name}"' if camera_name else None
lens_name = f'"{lens_name}"' if lens_name else None
if not image_data.country:
country_en = country_ru = None
country_en = f'"{image_data.country[\'en-US\']}"'
log.info('Adding user query to photo_queries_table...')
country_ru = f'"{image_data.country[\'ru-RU\']}"'
query = (
    'INSERT INTO photo_queries_table (chat_id, camera_name, lens_name, country_en, country_ru) VALUES (%s, %s, %s, %s, %s)'
    )
parameters = self.user.chat_id, camera_name, lens_name, country_en, country_ru
db.execute_query(query, parameters)
db.conn.commit()
log.info('User query was successfully added to the database.')
