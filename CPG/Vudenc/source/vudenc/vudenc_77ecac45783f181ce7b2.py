def get_common_objects(self):...
super().get_common_objects()
self.get_summary_submissions()
self.models = []
for url, name in self.exercise.get_models():
self.note('models')
response = request_for_response(url)
self.models.append({'name': name})
self.models.append({'name': name, 'content': response.text, 'html': 
    'text/html' in response.headers.get('Content-Type')})
