def get_person_instance(request):...
person_instance = None
person_instance = Person.objects.get(netid=request.user.username)
if 'orcid' in request.POST:
return person_instance
person_instance = Person.objects.get(orcid=request.POST['orcid'])
