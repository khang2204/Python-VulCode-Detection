@login_required...
from .forms import PersonForm, CandidateForm
if request.method == 'POST':
post_data = request.POST.copy()
shib_info = get_shib_info_from_request(request)
post_data['netid'] = request.user.username
person_instance = get_person_instance(request)
person_form = PersonForm(post_data, instance=get_person_instance(request))
degree_type = request.GET.get('type', '')
candidate_form = CandidateForm(post_data)
if person_instance:
if person_form.is_valid() and candidate_form.is_valid():
person_form = PersonForm(instance=person_instance, degree_type=degree_type)
person_form = PersonForm(initial=shib_info, degree_type=degree_type)
person = person_form.save()
return render(request, 'etd_app/register.html', {'person_form': person_form,
    'candidate_form': candidate_form, 'register': True})
candidate_form = CandidateForm(degree_type=degree_type)
banner_id = request.META.get('Shibboleth-brownBannerID', '')
if banner_id:
person.bannerid = banner_id
candidate = candidate_form.save(commit=False)
person.save()
candidate.person = person
candidate.save()
return HttpResponseRedirect(reverse('candidate_home', kwargs={
    'candidate_id': candidate.id}))
