@login_required...
if 'sort_by' in request.GET:
candidates = Candidate.get_candidates_by_status(status, sort_param=request.
    GET['sort_by'])
candidates = Candidate.get_candidates_by_status(status)
return render(request, 'etd_app/staff_view_candidates.html', {'candidates':
    candidates, 'status': status})
