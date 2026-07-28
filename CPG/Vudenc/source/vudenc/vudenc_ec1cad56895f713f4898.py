def get_people():...
people = []
ppl = User.query.all()
for person in ppl:
username = ''
return people
name = person.name
if person.username:
username = person.username
names = Name.query.filter_by(user_id=person.id)
people.append({'id': person.id, 'username': username, 'name': name, 'names':
    names})
