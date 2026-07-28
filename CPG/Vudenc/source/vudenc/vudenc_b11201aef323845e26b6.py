def get_common_objects(self):...
super().get_common_objects()
self.get_summary_submissions()
self.templates = []
for url, name in self.exercise.get_templates():
response = request_for_response(url)
self.note('templates')
self.templates.append({'name': name, 'content': response.text, 'html': 
    'text/html' in response.headers.get('Content-Type')})
