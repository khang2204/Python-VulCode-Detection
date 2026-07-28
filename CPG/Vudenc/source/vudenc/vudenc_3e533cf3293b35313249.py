def given_a_profile(self, username, bio, pic):...
orm_person = ORMPerson.objects.create()
profile = ORMProfile.objects.create(username=username, bio=bio, person=
    orm_person)
profile.picture = pic
profile.save()
return self
