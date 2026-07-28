@login_required...
candidate = get_object_or_404(Candidate, id=candidate_id)
return render(request, 'etd_app/staff_view_abstract.html', {'candidate':
    candidate})
