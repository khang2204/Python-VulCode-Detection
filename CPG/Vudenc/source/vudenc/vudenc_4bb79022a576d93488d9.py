@login_required...
from .forms import CommitteeMemberPersonForm, CommitteeMemberForm
candidate = _get_candidate(candidate_id=candidate_id, request=request)
return HttpResponseRedirect(reverse('register'))
if candidate.thesis.is_locked():
return HttpResponseForbidden('Thesis has already been submitted and is locked.'
    )
if request.method == 'POST':
person_form = CommitteeMemberPersonForm(request.POST)
person_form = CommitteeMemberPersonForm()
committee_member_form = CommitteeMemberForm(request.POST)
committee_member_form = CommitteeMemberForm()
if person_form.is_valid() and committee_member_form.is_valid():
context = {'candidate': candidate, 'person_form': person_form,
    'committee_member_form': committee_member_form}
person = person_form.save()
return render(request, 'etd_app/candidate_committee.html', context)
committee_member = committee_member_form.save(commit=False)
committee_member.person = person
committee_member.save()
candidate.committee_members.add(committee_member)
return HttpResponseRedirect(reverse('candidate_home', kwargs={
    'candidate_id': candidate.id}))
