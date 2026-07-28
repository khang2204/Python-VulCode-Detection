def _get_candidate(candidate_id, request):...
candidate = Candidate.objects.get(id=candidate_id)
if candidate.person.netid != request.user.username:
return candidate
