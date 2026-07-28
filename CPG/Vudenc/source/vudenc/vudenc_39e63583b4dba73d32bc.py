@login_required...
from .forms import PersonForm, CandidateForm
candidate = _get_candidate(candidate_id=candidate_id, request=request)
return HttpResponseRedirect(reverse('register'))
if candidate.thesis.is_locked():
return HttpResponseForbidden('Thesis has already been submitted and is locked.'
    )
if request.method == 'POST':
post_data = request.POST.copy()
shib_info = get_shib_info_from_request(request)
post_data['netid'] = request.user.username
degree_type = request.GET.get('type', '')
person_form = PersonForm(post_data, instance=candidate.person)
person_form = PersonForm(instance=candidate.person, degree_type=degree_type)
candidate_form = CandidateForm(post_data, instance=candidate)
candidate_form = CandidateForm(instance=candidate, degree_type=degree_type)
if person_form.is_valid() and candidate_form.is_valid():
return render(request, 'etd_app/register.html', {'person_form': person_form,
    'candidate_form': candidate_form})
person = person_form.save()
banner_id = request.META.get('Shibboleth-brownBannerID', '')
if banner_id:
person.bannerid = banner_id
candidate = candidate_form.save(commit=False)
person.save()
candidate.person = person
candidate.save()
return HttpResponseRedirect(reverse('candidate_home', kwargs={
    'candidate_id': candidate.id}))
