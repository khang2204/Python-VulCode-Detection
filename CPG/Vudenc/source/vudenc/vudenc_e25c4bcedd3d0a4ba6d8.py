@handle_html...
tags = []
mode = 'all'
for key, i in request.query.items():
if key == 'mode':
if not tags:
mode = i
if key == 'tag':
toilets = await database.select_toilet_statuses(request)
toilets = await database.select_toilet_statuses_by_tags(request, tags)
tags.append(i)
red, blue = [], []
for ID, lat, lng, name, status, dt in toilets:
(blue if status else red).append((ID, lat, lng, name, None))
out = '%s\n%s' % (mazemap.make_marker_chubs(red, color='red') if mode ==
    'all' else '', mazemap.make_marker_chubs(blue, color='blue'))
return mazemap.JS_skeleton.format(code=out)
