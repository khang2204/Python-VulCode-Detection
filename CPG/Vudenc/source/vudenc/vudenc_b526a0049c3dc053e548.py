def _build_json_response(self, query, access_for):...
json_response = []
for user in query:
applyDate = '-'
return json_response
access = access_for(user)
if not access:
access = access[0]
if access.access_requested:
applyDate = access.access_requested.strftime('%Y-%m-%d')
data = {'user': user.name, 'email': user.email, 'affiliation': user.
    affiliation, 'country': user.country, 'newsletter': access.
    wants_newsletter, 'has_access': access.has_access, 'applyDate': applyDate}
json_response.append(data)
