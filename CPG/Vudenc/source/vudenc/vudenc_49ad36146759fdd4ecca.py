def given_an_experience_on_db(self, title, description, share_id, pic):...
orm_person = ORMPerson.objects.create()
ORMProfile.objects.create(person=orm_person, username='u')
experience = ORMExperience.objects.create(title=title, description=
    description, share_id=share_id, author=orm_person)
experience.picture = pic
experience.save()
return self
